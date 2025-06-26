import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget
from ui_pilotage_frein_manuel import Ui_Form
import math
import mysql.connector
import time
from datetime import datetime 
import paho.mqtt.client as mqtt 

class AppPilotage(QWidget):
    def __init__(self, identifiant,moteur_choisi,role):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.identifiant = identifiant
        self.role = role
        self.moteur_choisi = moteur_choisi
        print(f"Rôle : {self.role}")  # Affichage en console
        self.client = mqtt.Client()
        self.client.username_pw_set("bancmoteur", "CestGenialCeBts2025")
        self.client.on_message = self.majSlider
        self.client.connect("192.168.2.108", 1883, 60)
        self.client.subscribe("Frein/CoeffA")
        self.client.loop_start()

        self.ui.gB_pilotage.setEnabled(False)
        self.ui.sB_valeurFrein.valueChanged.connect(self.modifierSpinBox)
        self.ui.slider_valeurFrein.valueChanged.connect(self.modifierSlider)
        self.ui.pb_marche_frein.clicked.connect(self.debutTest)
        self.ui.pb_arret_frein.clicked.connect(self.arretTest)
        self.ui.pb_valider_consigne_frein.clicked.connect(self.validerConsigne)
        self.ui.pb_retour_pilotage_frein.clicked.connect(self.retourAccueil)
        self.ui.pb_valider_enregistrement.clicked.connect(self.validerEnregistrement)
        self.show()

    def majSlider(self, client, userdata, msg):
        try:
            val = int(float(msg.payload.decode()))
            self.ui.slider_valeurFrein.setValue(val)
        except:
            pass

    def retourAccueil(self):
        if self.client is not None:
            self.client.loop_stop()
            self.client.disconnect()
            self.client = None

        if self.role == "prof":
            from CAccueil_prof import AppBancMotProf
            self.accueil = AppBancMotProf(self.identifiant, self.role, self.moteur_choisi)
        else:
            from CAccueil import AppBancMot
            self.accueil = AppBancMot(self.identifiant, self.role, self.moteur_choisi)

        self.accueil.show()
        self.close()

    def validerEnregistrement(self):
        choixEnregistrement = self.ui.cB_choix_enregistrement.currentIndex()
        if choixEnregistrement == 1:
            self.methodeEnregistrement = "continu"
            self.ui.gB_pilotage.setEnabled(True)
        elif choixEnregistrement == 2:
            self.methodeEnregistrement = "pointParPoint"
            self.ui.gB_pilotage.setEnabled(True)
        else:
            pass

    def debutTest(self):
        consigneFrein = self.ui.sB_valeurFrein.value()
        broker = "192.168.2.108"
        port = 1883
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        topic3 = "Frein/Etat"
        mqtt_username = "bancmoteur"
        mqtt_password = "CestGenialCeBts2025"

        self.client.publish(topic1, str(0))
        self.client.publish(topic2, str(consigneFrein))
        self.client.publish(topic3, str("Marche"))

        topics = ["Moteur/Ueff", "Moteur/Ieff", "Moteur/C", "Moteur/N", "Moteur/Numero"]
        topicEtatMoteur = "Moteur/Etat"
        topicNumeroMoteur = "Moteur/Numero"
        self.tension = []
        self.courant = []
        self.puissance = []
        self.couple = []
        self.vitesse = []

        self.temps = []
        self.temps_actuel = 0.0
        self.nb_donnees = 0

        if self.methodeEnregistrement == "continu":
            pass
        else:
            self.nb_donnees_max = 1  # une seule mesure

        self.client.on_message = self.on_message_received
        for topic in topics:
            self.client.subscribe(topic)
        self.valeurs_moteur = {
            "Moteur/Ueff": None,
            "Moteur/Ieff": None,
            "Moteur/C": None,
            "Moteur/N": None,
        }
        self.client.publish(topicEtatMoteur, "Marche")
        self.client.publish(topicNumeroMoteur, str(self.moteur_choisi))

    def on_message_received(self, client, userdata, message):
        try:
            topic = message.topic
            payload = message.payload.decode("utf-8")

            if topic in self.valeurs_moteur:
                self.valeurs_moteur[topic] = payload

                if all(value is not None for value in self.valeurs_moteur.values()):
                    try:
                        couple = float(self.valeurs_moteur['Moteur/C'])
                        vitesse = float(self.valeurs_moteur['Moteur/N'])
                        puissance_utile = couple * 2 * math.pi * (vitesse / 60)
                    except ValueError:
                        puissance_utile = 0.0

                    if self.methodeEnregistrement == "continu":
                        self.temps_actuel += 0.5

                    self.tension.append(self.valeurs_moteur['Moteur/Ueff'])
                    self.courant.append(self.valeurs_moteur['Moteur/Ieff'])
                    self.couple.append(self.valeurs_moteur['Moteur/C'])
                    self.vitesse.append(self.valeurs_moteur['Moteur/N'])
                    self.puissance.append(puissance_utile)
                    self.temps.append(self.temps_actuel)

                    texte = (
                        f"Tension : {self.valeurs_moteur['Moteur/Ueff']}\n"
                        f"Courant : {self.valeurs_moteur['Moteur/Ieff']}\n"
                        f"Couple : {self.valeurs_moteur['Moteur/C']}\n"
                        f"Vitesse : {self.valeurs_moteur['Moteur/N']}\n"
                        f"Puissance utile : {round(puissance_utile,1)} W\n"
                        f"Temps : {round(self.temps_actuel,1)} s\n"
                        f"-----"
                    )
                    self.ui.tE_valeur_temps_reel.append(texte)

                    self.nb_donnees += 1

                    if self.methodeEnregistrement == "point":
                        self.client.publish("Moteur/Etat", "Arret")
                        self.client.loop_stop()
                        self.client.disconnect()
                        self.client = None

                    for key in self.valeurs_moteur:
                        self.valeurs_moteur[key] = None

            elif topic == "Moteur/Numero":
                self.ui.tE_valeur_temps_reel.append(f"Numéro de moteur : {payload}\n")

        except Exception as e:
            print("Erreur réception MQTT :", e)

    def arretTest(self):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()

        if self.client is not None:
            try:
                self.client.loop_stop()
                self.client.disconnect()
                self.client = None
                self.ui.tE_valeur_temps_reel.append("Cycle arrêté")
            except Exception as e:
                self.ui.tE_valeur_temps_reel.append(f"Erreur lors de l'arrêt MQTT : {str(e)}")

        try:
            host = 'localhost'
            user = 'prof'
            db_password = 'CestGenialCeBts2025'
            database = 'eguidat_banc_moteur'
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=db_password,
                database=database
            )
            cursor = connection.cursor()
            date_essai = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            identifiant = self.identifiant
            tension = "[" + ";".join(self.tension) + "]"
            courant = "[" + ";".join(self.courant) + "]"
            couple = "[" + ";".join(self.couple) + "]"
            vitesse = "[" + ";".join(self.vitesse) + "]"
            puissance = "[" + ";".join(map(str, self.puissance)) + "]"
            temps = "[" + ";".join(map(str, self.temps)) + "]"
            moteur_choisi = self.moteur_choisi
            requete = """INSERT INTO essai (id_essai, date_essai, identifiant_eleve_essai, tension, courant, couple, vitesse_moteur, id_moteur, puissance, temps) 
                        VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(requete, (date_essai, identifiant, tension, courant, couple, vitesse, moteur_choisi, puissance, temps))
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            self.ui.tE_valeur_temps_reel.append(f"Erreur à l'arrêt du cycle : {str(e)}")

    def validerConsigne(self):
        valeur = int(self.ui.sB_valeurFrein.value())
        broker = "192.168.2.108"  
        port = 1883 
        topic1 = "Frein/Etat"
        topic2 = "Frein/Profil"
        topic3 = "Frein/CoeffA"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker, port, 60)
        client.publish(topic1, "Marche")
        client.publish(topic2, "0")
        client.publish(topic3, str(valeur))
        client.disconnect()

    def modifierSpinBox(self):
        valeur = int(self.ui.sB_valeurFrein.value())
        print(valeur)
        self.ui.slider_valeurFrein.setValue(valeur)

    def modifierSlider(self):
        valeur = int(self.ui.slider_valeurFrein.value())
        self.ui.sB_valeurFrein.setValue(valeur)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppPilotage()
    sys.exit(app.exec())
