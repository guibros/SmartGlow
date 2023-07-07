
"""
Ce fichier crée la classe d'accès à la base de données ainsi 
que les méthodes utilisées pour insérer un nouveau client dans
la base de données. Il a également la méthode nécessaire pour
trouver un client qui a été inséré dans la base de données. 
Utilisez ce fichier pour entrer des clients dans la base de
données aux fins du projet intégrateur.
"""

from pymongo import MongoClient as mongo


# CREATION OF RPA CLASS

class RPA:
    def __init__(self):
        URI = "mongodb+srv://Phil:Sp9IFET6c7ceIWQa@maiya.engxn.mongodb.net/?retryWrites=true&w=majority"
        client = mongo(URI)
        db = client.RPA
        self.collection = db['RPA Clients']
    
    
    def insertNewClient(self, keyName, firstName, lastName, phone, address,
                        friend_1='n/a', fr_last_1= 'n/a', fr_phone_1='n/a', fr_type1='n/a',
                        friend_2='n/a', fr_last_2= 'n/a', fr_phone_2='n/a', fr_type2='n/a',
                        friend_3='n/a', fr_last_3= 'n/a', fr_phone_3='n/a', fr_type3='n/a',
                        family_1='n/a', fa_last_1= 'n/a', fa_phone_1='n/a', fa_type1='n/a',
                        family_2='n/a', fa_last_2= 'n/a', fa_phone_2='n/a', fa_type2='n/a',
                        family_3='n/a', fa_last_3= 'n/a', fa_phone_3='n/a', fa_type3='n/a',
                        medical_1='n/a', me_last_1= 'n/a', me_phone_1='n/a', me_type1='n/a',
                        medical_2='n/a', me_last_2= 'n/a', me_phone_2='n/a', me_type2='n/a',
                        medical_3='n/a', me_last_3= 'n/a', me_phone_3='n/a', me_type3='n/a',
                        emergency_1='n/a', em_last_1= 'n/a', em_phone_1='n/a', em_type1='n/a',
                        emergency_2='n/a', em_last_2= 'n/a', em_phone_2='n/a', em_type2='n/a',
                        emergency_3='n/a', em_last_3= 'n/a', em_phone_3='n/a', em_type3='n/a',
                        medication_1='n/a', dosageMed_1='n/a',
                        medication_2='n/a', dosageMed_2='n/a',
                        medication_3='n/a', dosageMed_3='n/a',
                        appointment_1='n/a', date_1='n/a', time_1= 'n/a', place_1='n/a',
                        appointment_2='n/a', date_2='n/a', time_2= 'n/a', place_2='n/a',
                        appointment_3='n/a', date_3='n/a', time_3= 'n/a', place_3='n/a',
                        activity_1='n/a', ac_date_1='n/a', ac_time_1= 'n/a', ac_place_1='n/a',
                        activity_2='n/a', ac_date_2='n/a', ac_time_2= 'n/a', ac_place_2='n/a',
                        activity_3='n/a', ac_date_3='n/a', ac_time_3= 'n/a', ac_place_3='n/a'):
        new_client = {  'ClientInfo': {
                            'keyName': keyName, 'firstName': firstName,
                            'lastName':lastName,'Telephone': phone, 'address': address
                        },
                        'Contacts': {
                                'Contact_1': {'Name': friend_1, 'Last': fr_last_1, 'Telephone': fr_phone_1, 'Type': fr_type1},
                                'Contact_2': {'Name': friend_2, 'Last': fr_last_2, 'Telephone': fr_phone_2, 'Type': fr_type2},
                                'Contact_3': {'Name': friend_3, 'Last': fr_last_3, 'Telephone': fr_phone_3, 'Type': fr_type3},
                                'Contact_4': {'Name': family_1, 'Last': fa_last_1, 'Telephone': fa_phone_1, 'Type': fa_type1},
                                'Contact_5': {'Name': family_2, 'Last': fa_last_2, 'Telephone': fa_phone_2, 'Type': fa_type2},
                                'Contact_6': {'Name': family_3, 'Last': fa_last_3, 'Telephone': fa_phone_3, 'Type': fa_type3},
                                'Contact_7': {'Name': medical_1, 'Last': me_last_1, 'Telephone': me_phone_1, 'Type': me_type1},
                                'Contact_8': {'Name': medical_2, 'Last': me_last_2, 'Telephone': me_phone_2, 'Type': me_type2},
                                'Contact_9': {'Name': medical_3, 'Last': me_last_3, 'Telephone': me_phone_3, 'Type': me_type3},
                                'Contact_10': {'Name': emergency_1, 'Last': em_last_1, 'Telephone': em_phone_1, 'Type': em_type1},
                                'Contact_11': {'Name': emergency_2, 'Last': em_last_2, 'Telephone': em_phone_2, 'Type': em_type2},
                                'Contact_12': {'Name': emergency_3, 'Last': em_last_3, 'Telephone': em_phone_3, 'Type': em_type3}
                            },
                        'Medication': {
                            'Medication_1': {'Name': medication_1, 'Dosage': dosageMed_1},
                            'Medication_2': {'Name': medication_2, 'Dosage': dosageMed_2},
                            'Medication_3': {'Name': medication_3, 'Dosage': dosageMed_3}
                        },
                        'Appointments': {
                            'Appointment_1': {'Name': appointment_1, 'Date': date_1, 'Time': time_1, 'Location': place_1},
                            'Appointment_2': {'Name': appointment_2, 'Date': date_2, 'Time': time_2, 'Location': place_2},
                            'Appointment_3': {'Name': appointment_3, 'Date': date_3, 'Time': time_3, 'Location': place_3}
                        },
                        'Activity': {
                            'Activity_1': {'Name': activity_1, 'Date': ac_date_1, 'Time': ac_time_1, 'Location': ac_place_1},
                            'Activity_2': {'Name': activity_2, 'Date': ac_date_2, 'Time': ac_time_2, 'Location': ac_place_2},
                            'Activity_3': {'Name': activity_3, 'Date': ac_date_3, 'Time': ac_time_3, 'Location': ac_place_3}
                        }
                    }
        self.collection.insert_one(new_client)
        
    def findClient(self, keyName):
        user = self.collection.find_one({"ClientInfo.keyName": keyName})
        return user


if __name__ == '__main__':
    
    # INSTANTIATE CLASS
    RPA_db = RPA()
    
    # INSERT CLIENTS INTO DATABASE
    # RPA_db.insertNewClient( 'Phil', 'Phil', 'Doe', '514-564-8656', '123 RPA street, Montreal, Quebec, H1H 1H1',
    #                         friend_1='Nancy', fr_last_1='Smith', fr_phone_1='514-222-3456', fr_type1='connaissance',
    #                         friend_2='Harry', fr_last_2='Klein', fr_phone_2='514-333-7547', fr_type2='connaissance',
    #                         friend_3='George', fr_last_3='Ramos', fr_phone_3='514-444-8685', fr_type3='connaissance',
    #                         family_1='Jim', fa_last_1='Doe', fa_phone_1='514-555-5745', fa_type1='famille',
    #                         family_2='Larry', fa_last_2='Doe', fa_phone_2='514-666-9867', fa_type2='famille',
    #                         family_3='Stephanie', fa_last_3='Doe', fa_phone_3='514-777-4354', fa_type3='famille',
    #                         medical_1='Dr. John', me_last_1='Miles, Generaliste', me_phone_1='514-888-9876', me_type1='médical',
    #                         medical_2='Dr. Harry', me_last_2='Kravitz, Neurologue', me_phone_2='514-234-2452', me_type2='médical',
    #                         medical_3='Dr. Liz', me_last_3='Nancy, Nephrologue', me_phone_3='514-432-7355', me_type3='médical',
    #                         emergency_1='Billy', em_last_1='Doe', em_phone_1='514-567-2432', em_type1='urgence',
    #                         emergency_2='Evelyne', em_last_2='Richards', em_phone_2='765-111-7546', em_type2='urgence',
    #                         emergency_3='Lisa', em_last_3='Kuds', em_phone_3='795-564-1234', em_type3='urgence',
    #                         medication_1='Valium XR', dosageMed_1="Prenez un comprimé par voie orale trois fois par jour avant les repas.",
    #                         medication_2='Motrin', dosageMed_2="Injectez une dose de 1 ml par voie intramusculaire tous les deux jours.",
    #                         medication_3='Nalaproxen', dosageMed_3="Appliquez une petite quantité de crème sur la zone affectée deux fois par jour.",
    #                         appointment_1='Dermatolgue', date_1='Lundi, 4 février, 2023', time_1='14:00', place_1='CLSC Montreal',
    #                         appointment_2='Psychiatre', date_2='Vendredi, 6 mars, 2023', time_2='13h00', place_2='Notre-Dame Hospital',
    #                         appointment_3='Neurologue', date_3='Jeudi, 11 avril, 2023', time_3='8h30', place_3='Downtown Medical Clinic',
    #                         activity_1='Souper spagetti', ac_date_1='Vendredi le 18 mars', ac_time_1= '17h00', ac_place_1='Cafeteria',
    #                         activity_2='Curling', ac_date_2='Samedi le 19 mars', ac_time_2= '10h00', ac_place_2='Arena',
    #                         activity_3='Bingo', ac_date_3='Dimanche le 20 mars', ac_time_3= '13h00', ac_place_3='Salle Communautaire')


    # RPA_db.insertNewClient( 'Guillaume', 'Guillaume', 'Brunet', '514-333-8656', '3221 rue Pagot, Montreal, Quebec, H2L 3X9',
    #                         friend_1='Marie', fr_last_1='Dubois', fr_phone_1='514-987-3456', fr_type1='connaissance',
    #                         friend_2='Francois', fr_last_2='Tremblay', fr_phone_2='514-876-7547', fr_type2='connaissance',
    #                         friend_3='Sophie', fr_last_3='Bouchard', fr_phone_3='514-765-8685', fr_type3='connaissance',
    #                         family_1='Pierre', fa_last_1='Martin', fa_phone_1='514-655-6544', fa_type1='famille',
    #                         family_2='Isabelle', fa_last_2='Martin', fa_phone_2='514-543-9867', fa_type2='famille',
    #                         family_3='Nathalie', fa_last_3='Martin', fa_phone_3='514-432-4354', fa_type3='famille',
    #                         medical_1='Dr. Luc', me_last_1='Lacroix, Cardiologue', me_phone_1='514-888-9876', me_type1='médical',
    #                         medical_2='Dr. Caroline', me_last_2='Roy, Pédiatre', me_phone_2='514-234-2452', me_type2='médical',
    #                         medical_3='Dr. Michel', me_last_3='Blanchet, Chirurgien', me_phone_3='514-432-7355', me_type3='médical',
    #                         emergency_1='Julie', em_last_1='Bergeron', em_phone_1='514-567-2432', em_type1='urgence',
    #                         emergency_2='Jean-Francois', em_last_2='Dufour', em_phone_2='765-111-7546', em_type2='urgence',
    #                         emergency_3='Alexandre', em_last_3='Gagne', em_phone_3='795-564-1234', em_type3='urgence',
    #                         medication_1='Paracetamol', dosageMed_1="Utilisez l'inhalateur deux fois par jour ou selon les besoins.",
    #                         medication_2='Ibuprofène', dosageMed_2="Prenez un comprimé à libération prolongée une fois par jour avant le coucher.",
    #                         medication_3='Amoxicilline', dosageMed_3="Prenez un comprimé par voie orale chaque matin avec un verre d'eau.",
    #                         appointment_1='Urolgue', date_1='Mercredi, 14 mars, 2023', time_1='11:30', place_1='CHUM Montreal',
    #                         appointment_2='Ophtalmologiste', date_2='Dimanche, 16 mars, 2023', time_2='12h40', place_2='Hospital Sacré-Coeur',
    #                         appointment_3='Othopédiste', date_3='Samedi, 21 avril, 2023', time_3='18h35', place_3='Clinic du Plateau',
    #                         activity_1='Marche communautaire', ac_date_1='Jeudi le 8 mai', ac_time_1= '19h30', ac_place_1='Cour éxtérieure',
    #                         activity_2='Tai-Chi', ac_date_2='Samedi le 19 mars', ac_time_2= '11h20', ac_place_2='Salle de détente',
    #                         activity_3='Yoga', ac_date_3='Dimanche le 20 mars', ac_time_3= '14h50', ac_place_3='Salle Communautaire')

    # RPA_db.insertNewClient( 'DEFAULT', 'DEFAULT', 'DEFAULT', 'DEFAULT', 'DEFAULT')
    
    # RPA_db.insertNewClient( 'xxxxx', 'xxxxxxx', 'xxxxxx', '514-564-8656', '1253 Gaspé street, Montreal, Quebec, H2H 2H2',
    #                         friend_1='Pierre', fr_last_1='Trudeau', fr_phone_1='514-222-3456', fr_type1='connaissances',
    #                         friend_2='Celine', fr_last_2='Dion', fr_phone_2='514-333-7547', fr_type2='connaissances',
    #                         friend_3='Guy', fr_last_3='Lafleur', fr_phone_3='514-444-8685', fr_type3='connaissances',
    #                         family_1='Ryan', fa_last_1='Reynolds', fa_phone_1='514-555-5745', fa_type1='famille',
    #                         family_2='Micahel', fa_last_2='Fox', fa_phone_2='514-666-9867', fa_type2='famille',
    #                         family_3='Leo', fa_last_3='Cohan', fa_phone_3='514-777-4354', fa_type3='famille',
    #                         medical_1='Dr. Rich', me_last_1='Voisin, Cardiologue', me_phone_1='514-888-9876', me_type1='médical',
    #                         medical_2='Dr. Yann', me_last_2='Noah, Pédiatre', me_phone_2='514-234-2452', me_type2='médical',
    #                         medical_3='Dr. Karine', me_last_3='Vaany, Psychiatre', me_phone_3='514-432-7355', me_type3='médical',
    #                         emergency_1='Normand', em_last_1='Bourg', em_phone_1='514-567-2432', em_type1='urgence',
    #                         emergency_2='Luc', em_last_2='Plama', em_phone_2='765-111-7546', em_type2='urgence',
    #                         emergency_3='Guillaume', em_last_3='Cane', em_phone_3='795-564-1234', em_type3='urgence',
    #                         medication_1='Tylennol', dosageMed_1="Prenez un comprimé deux fois par jour.",
    #                         medication_2='Advil', dosageMed_2="Injectez une dose tous les deux jours.",
    #                         medication_3='Moxicilline', dosageMed_3="Un comprimé avant de se coucher.",
    #                         appointment_1='Endocrinologue', date_1='Vendredi, 14 février, 2023', time_1='14:00', place_1='CLSC Lasalle',
    #                         appointment_2='Rhumatologue', date_2='Samedi, 16 mars, 2023', time_2='13h00', place_2='McGill Hospital',
    #                         appointment_3='Infectiologue', date_3='Dimanche, 21 avril, 2023', time_3='8h30', place_3='Chomedy Medical Clinic',
    #                         activity_1='Souper', ac_date_1='Lundi le 28 mars', ac_time_1= '17h00', ac_place_1='Salle à manger',
    #                         activity_2='Bowling', ac_date_2='Vendredi le 29 mars', ac_time_2= '10h00', ac_place_2='Bowlodrome',
    #                         activity_3='Casino', ac_date_3='Dimanche le 21 mars', ac_time_3= '13h00', ac_place_3='Casino de Montréal')


    # RPA_db.insertNewClient( 'xxxxxxxxx', 'xxxxxxxx', 'xxxxxxxx', '514-333-8656', '3123 rue Loviere, Montreal, Quebec, H2P 3P9',
    #                         friend_1='Denis', fr_last_1='Ville', fr_phone_1='514-987-3456', fr_type1='connaissances'
    #                         friend_2='Sophie', fr_last_2='Marc', fr_phone_2='514-876-7547', fr_type2='connaissances',
    #                         friend_3='Isa', fr_last_3='Blay', fr_phone_3='514-765-8685', fr_type3='connaissances',
    #                         family_1='Pierre', fa_last_1='Lapointe', fa_phone_1='514-655-6544', fa_type1='famille',
    #                         family_2='Mari', fa_last_2='Wolf', fa_phone_2='514-543-9867', fa_type2='famille',
    #                         family_3='Steph', fa_last_3='Rousseaum', fa_phone_3='514-432-4354', fa_type3='famille',
    #                         medical_1='Dr. Max', me_last_1='Martin, Radiologue', me_phone_1='514-888-9876', me_type1='médical',
    #                         medical_2='Dr. Isabelle', me_last_2='Hope, Anesthésiste', me_phone_2='514-234-2452', me_type2='médical',
    #                         medical_3='Dr. Claude', me_last_3='Blanchet, Dermatologue', me_phone_3='514-432-7355', me_type3='médical',
    #                         emergency_1='Alex', em_last_1='Bergeron', em_phone_1='514-567-2432', em_type1='urgence',
    #                         emergency_2='Jean', em_last_2='Dufour', em_phone_2='765-111-7546', em_type2='urgence',
    #                         emergency_3='Francois', em_last_3='Gagne', em_phone_3='795-564-1234', em_type3='urgence',
    #                         medication_1='Aspirine', dosageMed_1="Un comprimé deux fois par jour ou selon les besoins.",
    #                         medication_2='Acétaminophène', dosageMed_2="Prenez un comprimé avant le coucher.",
    #                         medication_3='Lisinopril', dosageMed_3="Prenez un comprimé par voie orale.",
    #                         appointment_1='Gastro-entérologue', date_1='Jeudi, 12 mars, 2023', time_1='11:30', place_1='Hopital Victoria Montreal',
    #                         appointment_2='Allergologue', date_2='Vendredi, 19 mars, 2023', time_2='12h40', place_2='Hospital Maissoneuve',
    #                         appointment_3='Néphrologue', date_3='Mercredi, 22 avril, 2023', time_3='18h35', place_3='Clinic de Verdun',
    #                         activity_1='Ping Pong', ac_date_1='Samedi le 18 mai', ac_time_1= '19h30', ac_place_1='Cour',
    #                         activity_2='Meditation', ac_date_2='Mardi le 18 mars', ac_time_2= '11h20', ac_place_2='Salle de meditation',
    #                         activity_3='Massage', ac_date_3='Mercredi le 23 mars', ac_time_3= '14h50', ac_place_3='Salle de relaxation')