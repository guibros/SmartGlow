"""
Ce fichier est le fichier de boucle principal pour tout ce
qui concerne la reconnaissance faciale.
Il se connecte à MQTT pour envoyer l'état
de la reconnaissance faciale.
"""

from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
from mqttConfig import MQTTcontroller
from log_Monitor import Monitor


# Set up log-monitor
monitor = Monitor()
logger = monitor.logger('log_FacialStatus')


class Recognizer:
    def __init__(self):
        self.currentName = 'Unknown'
        self.cam = ''
        self.initial_PROXI_Time = time.time()
        self.initial_OBJECT_Time = time.time()
        self.PROXIMITY_WAIT_TIME = 5
        self.OBJECT_WAIT_TIME = 10
        self.Identifying = True
        
    def forAtLeast_x_seconds(self, seconds, initialTime):
        currenTime = time.time()
        timeDifference = round(currenTime - initialTime)
        if timeDifference >= seconds:
            return True
        return False

    def run(self):
        currentname = "unknown"
        encodingsP = "/home/pi/Documents/FacialRecognition/Facial_module/encodings.pickle"
        
        logger.debug("\n\nFacial Recognition Activated")
        
        data = pickle.loads(open(encodingsP, "rb").read(), encoding='utf-8')
        vs = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)
        fps = FPS().start()
        
        #MQTT
        Proximity = MQTTcontroller(default='noProximity')
        Proximity.subscription('AHUNTSIC-PROJ-INT/proximity')

        # loop over frames from the video file stream
        while True:
            frame = vs.read()
            frame = imutils.resize(frame, width=500)
            boxes = face_recognition.face_locations(frame)
            encodings = face_recognition.face_encodings(frame, boxes)
            names = []
            
            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"],encoding)
                name = "Unknown" 
                
                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    name = max(counts, key=counts.get)

                    if currentname != name:
                        currentname = name
                    
                # update the list of names
                names.append(name)
                
            if 'noProximity' in Proximity.message:
                Proximity.publish('AHUNTSIC-PROJ-INT/identity', 'Nothing')
                self.initial_PROXI_Time = time.time()
                self.initial_OBJECT_Time = time.time()
                logger.debug('Nothing in proximity')
            elif 'proximityDetected' in Proximity.message:
                logger.debug(f"********** NAMES = {names}")
                if len(names) > 0:  # If there is a face
                    if self.Identifying:
                        Proximity.publish('AHUNTSIC-PROJ-INT/identity', 'IdentificationDelay')
                    while 'Unknown' in names and len(names) > 1:
                        names.remove('Unknown')
                    if self.forAtLeast_x_seconds(self.PROXIMITY_WAIT_TIME, self.initial_PROXI_Time):  # for x secs
                        self.Identifying = False
                        if names[0] == 'Unknown':  # names[0] means: if the closes face
                            Proximity.publish('AHUNTSIC-PROJ-INT/identity', 'Unknown')
                            self.initial_PROXI_Time = time.time()  
                            logger.debug('Unknown face in proximity')
                        elif names[0] != 'Unknown':
                            Proximity.publish('AHUNTSIC-PROJ-INT/identity', f"{names[0]}")
                            self.initial_PROXI_Time = time.time()
                            logger.debug(f'Known face: {names[0]} in proximity.')
                    self.initial_OBJECT_Time = time.time()
                elif len(names) == 0:
                    self.initial_PROXI_Time = time.time()
                    if self.forAtLeast_x_seconds(self.OBJECT_WAIT_TIME, self.initial_OBJECT_Time):  # If there is no face for x secs.
                        Proximity.publish('AHUNTSIC-PROJ-INT/identity', 'Object')
                        self.initial_PROXI_Time = time.time()
                        self.initial_OBJECT_Time = time.time()
                        self.Identifying = True
                        logger.debug('Object in front')

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                # draw the predicted face name on the image - color is in BGR
                cv2.rectangle(frame, (left, top), (right, bottom),
                    (0, 255, 225), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                    .8, (0, 255, 255), 2)

            # display the image to our screen
            cv2.imshow("Facial Recognition is Running", frame)
            key = cv2.waitKey(1) & 0xFF

            # quit when 'q' key is pressed
            if key == ord("q") or self.cam == 'kill':
                print("\nCamera shut off")
                break

            # update the FPS counter
            fps.update()

        # stop the timer and display FPS information
        fps.stop()

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()
        logger.debug('\nFacial recognition has ended')
        return

if __name__ == '__main__':
    recognizer = Recognizer()
    recognizer.run()