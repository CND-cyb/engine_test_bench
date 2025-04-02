import sys
from PySide6.QtWidgets import QApplication, QWidget
from choix_moteur_ui import Ui_Form
import paho.mqtt.client as mqtt 

class AppChoixMoteur(QWidget):
    def __init__(self,identifiant):
        super().__init__()
        #Utilisation de Ui_Ui_utilisationQTableWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.identifiant = identifiant  
        self.ui.pb_valider_machine.clicked.connect(self.choisirMoteur)
        self.show()
        print(f"Utilisateur connecté : {self.identifiant}")  # Affichage en console"""


    def choisirMoteur(self):
        moteurs = {
            self.ui.rB_moteur1: 1,
            self.ui.rB_moteur2: 2,
            self.ui.rB_moteur3: 3,
            self.ui.rB_moteur4: 4,
            self.ui.rB_moteur5: 5,
            self.ui.rB_moteur6: 6,
            self.ui.rB_moteur7: 7,
            self.ui.rB_moteur8: 8
        }
        moteur_choisi=""
        for radio_button,valeur in moteurs.items():
            if radio_button.isChecked():
                moteur_choisi=valeur
        if moteur_choisi!="":
            print("Moteur sélectionné :",moteur_choisi)
            self.publish_to_mqtt(moteur_choisi)
        from CAccueil_prof import AppBancMotProf
        self.accueil=AppBancMotProf(self.identifiant,moteur_choisi)
        self.accueil.show()
        self.close()
            
            
    def retourAccueil(self,identifiant):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(identifiant)
        self.accueil.show()
        self.close()
        
    def publish_to_mqtt(self, moteur_choisi):
        broker = "192.168.2.100"  
        port = 1883 
        topic = "Moteur/Numero"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        payload = str(moteur_choisi)  
        client.publish(topic, payload)
        client.disconnect()
        
        
#programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppChoixMoteur()
    sys.exit(app.exec())
