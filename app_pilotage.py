import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_pilotage_frein_manuel import Ui_Form
import paho.mqtt.client as mqtt 

class AppPilotage(QWidget):
    def __init__(self,identifiant):
        super().__init__()
        #Utilisation de Ui_Ui_utilisationQTableWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.identifiant=identifiant
        self.ui.sB_valeurFrein.valueChanged.connect(self.modifierSpinBox)
        self.ui.slider_valeurFrein.valueChanged.connect(self.modifierSlider)
        self.ui.pb_marche_frein.clicked.connect(self.debutTest)
        self.ui.pb_arret_frein.clicked.connect(self.arretTest)
        self.ui.pb_valider_consigne_frein.clicked.connect(self.validerConsigne)
        self.ui.pb_retour_pilotage_frein(self.retour)
        self.show()
        
    def retour(self):
          pass
    
    def debutTest(self):
        consigneFrein=self.ui.sB_valeurFrein.value()
        print(consigneFrein)
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/profil"
        topic2 = "Frein/coeffA"
        topic3 = "Frein/etat"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(0))
        client.publish(topic2,str(consigneFrein))
        client.publish(topic3,str("Marche"))
        client.disconnect()
        
    def arretTest(self):
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/etat"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str("Arret"))
        client.disconnect()
        
    def validerConsigne(self):
        valeur=int(self.ui.sB_valeurFrein.value())
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/etat"
        topic2 = "Frein/profil"
        topic3 = "Frein/coeffA"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str("Marche"))
        client.publish(topic2, str("0"))
        client.publish(topic3, str(valeur))
        client.disconnect()
        
    def modifierSpinBox(self):
        valeur = int(self.ui.sB_valeurFrein.value())
        print(valeur)
        self.ui.slider_valeurFrein.setValue(valeur)

    def modifierSlider(self):
        valeur = int(self.ui.slider_valeurFrein.value())
        self.ui.sB_valeurFrein.setValue(valeur)
        
#programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppPilotage()
    sys.exit(app.exec())
