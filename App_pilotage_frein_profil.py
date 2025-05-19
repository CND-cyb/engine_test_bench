import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap
from pilotage_frein_profil_ui import Ui_Form
import paho.mqtt.client as mqtt 


class AppPilotageProfil(QWidget):
    def __init__(self,identifiant,moteur_choisi):
        super().__init__()
        self.identifiant=identifiant
        self.moteur_choisi=moteur_choisi
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tabWidget.setEnabled(True)  
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabEnabled(i, False)
        self.ui.pb_choisir_frein_profil.clicked.connect(self.choisirProfil)
        self.ui.pb_retour_profil1.clicked.connect(self.retourChoixProfil)
        self.ui.pb_retour_profil2.clicked.connect(self.retourChoixProfil)
        self.ui.pb_retour_profil3.clicked.connect(self.retourChoixProfil)
        self.ui.pb_retour_profil4.clicked.connect(self.retourChoixProfil)        
        self.ui.pb_retour_profil5.clicked.connect(self.retourChoixProfil)
        self.ui.pb_frein_profil_quitter.clicked.connect(self.quitter)
        self.ui.pb_valider_profil1.clicked.connect(self.validerProfil1)
        self.ui.pb_valider_profil2.clicked.connect(self.validerProfil2)
        self.ui.pb_valider_profil3.clicked.connect(self.validerProfil3)
        self.ui.pb_valider_profil4.clicked.connect(self.validerProfil4)
        self.ui.pb_valider_profil5.clicked.connect(self.validerProfil5)
        self.ui.tabWidget.setCurrentIndex(0)
        label_image_profil1=self.ui.l_image_profil1
        pixmap1 = QPixmap("C:/pyqt6/banc_moteur-main/constant.png")  # Remplace par ton chemin d'image
        label_image_profil1.setPixmap(pixmap1)
        label_image_profil1.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil2=self.ui.l_image_profil2
        pixmap2 = QPixmap("C:/pyqt6/banc_moteur-main/affine.png")  # Remplace par ton chemin d'image
        label_image_profil2.setPixmap(pixmap2)
        label_image_profil2.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil3=self.ui.l_image_profil3
        pixmap3 = QPixmap("C:/pyqt6/banc_moteur-main/expo.png")  # Remplace par ton chemin d'image
        label_image_profil3.setPixmap(pixmap3)
        label_image_profil3.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil4=self.ui.l_image_profil4
        pixmap4 = QPixmap("C:/pyqt6/banc_moteur-main/bizarre.png")  # Remplace par ton chemin d'image
        label_image_profil4.setPixmap(pixmap4)
        label_image_profil4.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil5=self.ui.l_image_profil5
        pixmap5 = QPixmap("C:/pyqt6/banc_moteur-main/cyclique.png")  # Remplace par ton chemin d'image
        label_image_profil5.setPixmap(pixmap5)
        label_image_profil5.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        
        self.show()

    def choisirProfil(self):
        index = self.ui.cB_choix_profil.currentIndex()
        if 0 <= index < self.ui.tabWidget.count():
            for i in range(self.ui.tabWidget.count()):
                self.ui.tabWidget.setTabEnabled(i, False)
            self.ui.tabWidget.setTabEnabled(index, True)
            self.ui.tabWidget.setCurrentIndex(index)
            
    def validerProfil1(self):
        profil1_coefA=self.ui.sB_consigneFrein.value()
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(1))
        client.publish(topic2,str(profil1_coefA))
        client.disconnect()
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.accueil.demarrerCycle()
        self.close()
        
    def validerProfil2(self):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.accueil.demarrerCycle()        
        self.close()
        def incrementationProfil2():
            broker = "192.168.2.100"  
            port = 1883 
            mqtt_username = "bancmoteur" 
            mqtt_password = "CestGenialCeBts2025" 
            client = mqtt.Client()
            client.username_pw_set(mqtt_username, mqtt_password)
            client.connect(broker,port,60)
            client.publish("Frein/Profil",str(2))
            pourcentageFinal=self.ui.sB_consigneFreinFin_profil2.value()
            b = self.ui.sB_consigneFreinDepart_profil2.value()           # Pourcentage de départ
            a = (pourcentageFinal - b) / 10                               # Calcul automatique pour atteindre 100%
            self.t = 0
            def incrementerProfil2():
                if self.t > 10:
                    timer.stop()
                    return
                pourcentage = a * self.t + b
                pourcentage = min(pourcentage, 100)  # Sécurité anti dépassement
                client.publish("Frein/CoeffA", str(round(pourcentage, 2)))
                self.t += 1
            timer = QTimer()
            timer.timeout.connect(incrementerProfil2)
            timer.start(1000)
        QTimer.singleShot(0, incrementationProfil2)

        
    def validerProfil3(self):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.accueil.demarrerCycle()
        self.close()
        def incrementationProfil3():
            broker = "192.168.2.100"  
            port = 1883 
            mqtt_username = "bancmoteur" 
            mqtt_password = "CestGenialCeBts2025" 
            client = mqtt.Client()
            client.username_pw_set(mqtt_username, mqtt_password)
            client.connect(broker,port,60)
            client.publish("Frein/Profil",str(3))
            pourcentageFinal=self.ui.sB_consigneFreinFin_profil3.value()
            b = self.ui.sB_consigneFreinDepart_profil3.value()           # Pourcentage de départ
            a = (pourcentageFinal - b) / (10**2)                               # Calcul automatique pour atteindre 100%
            self.t = 0
            def incrementerProfil3():
                if self.t > 10:
                    timer.stop()
                    return
                pourcentage = a *(self.t**2)+b
                pourcentage = min(pourcentage, 100)  # Sécurité anti dépassement
                client.publish("Frein/CoeffA", str(round(pourcentage, 2)))
                self.t += 1
            timer = QTimer()
            timer.timeout.connect(incrementerProfil3)
            timer.start(1000)
        QTimer.singleShot(0, incrementationProfil3)

    def validerProfil4(self):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.accueil.demarrerCycle()   
        self.close()
        def incrementationProfil4():
            broker = "192.168.2.100"
            port = 1883
            mqtt_username = "bancmoteur"
            mqtt_password = "CestGenialCeBts2025"
            client = mqtt.Client()
            client.username_pw_set(mqtt_username, mqtt_password)
            client.connect(broker, port, 60)
            client.publish("Frein/Profil", str(4))
            coef_depart = self.ui.sB_consigneFreinDepart_profil4.value()
            coef_final = self.ui.sB_consigneFreinFin_profil4.value()
            A = 10 * coef_final
            self.t = 0
            def incrementerProfil4():
                if self.t > 10:
                    timer.stop()
                    return
                if self.t == 0:
                    pourcentage = coef_depart
                else:
                    pourcentage = A / self.t
                    pourcentage = min(pourcentage, coef_depart)
                client.publish("Frein/CoeffA", str(round(pourcentage, 2)))
                self.t += 1
            timer = QTimer()
            timer.timeout.connect(incrementerProfil4)
            timer.start(1000)
        QTimer.singleShot(0, incrementationProfil4)

        
    def validerProfil5(self):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.accueil.demarrerCycle()   
        self.close()
        def incrementationProfil5():
            broker = "192.168.2.100"
            port = 1883
            mqtt_username = "bancmoteur"
            mqtt_password = "CestGenialCeBts2025"
            client = mqtt.Client()
            client.username_pw_set(mqtt_username, mqtt_password)
            client.connect(broker, port, 60)
            client.publish("Frein/Profil", str(5))
            coef_haut = self.ui.sB_coefficientFreinEtatHaut_profil5.value()
            coef_bas = self.ui.sB_coefficientFreinEtatBas_profil5.value()
            rapport = self.ui.sB_rapportCyclique_profil5.value()  # en %
            tempsEtatHaut = round((rapport / 100) * 10)
            tempsEtatBas = 10 - tempsEtatHaut
            sequence = [coef_haut] * tempsEtatHaut + [coef_bas] * tempsEtatBas
            sequence = sequence[:10]  # Sécurité
            self.t = 0
            def incrementerProfil5():
                if self.t >= len(sequence):
                    timer.stop()
                    return
                pourcentage = sequence[self.t]
                client.publish("Frein/CoeffA", str(round(pourcentage, 2)))
                self.t += 1
            timer = QTimer()
            timer.timeout.connect(incrementerProfil5)
            timer.start(1000)
        QTimer.singleShot(0, incrementationProfil5)

    
    def retourChoixProfil(self):
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabEnabled(i, False)
        
    def quitter(self):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
        
# Programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppPilotageProfil()
    sys.exit(app.exec())
