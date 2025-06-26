import sys
import qrcode
import pyotp  
import mysql.connector
import bcrypt
import csv 
from datetime import datetime
import math
import time 
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem,QTableWidget, QComboBox, QLineEdit, QVBoxLayout, QCheckBox, QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt 
from accueil import Ui_AppBancMot
from app_pilotage import AppPilotage
from App_pilotage_frein_profil import AppPilotageProfil

class AppBancMot(QWidget):
    def __init__(self, identifiant,role,moteur_choisi=None):
        super().__init__()
        self.ui = Ui_AppBancMot()  
        self.ui.setupUi(self)  # Configure l'interface
        self.recuperer_donnee()
        self.recuperer_moteur()
        self.essaiSelectionne=None
        self.identifiant=identifiant  # Stocker l'identifiant
        self.role=role # Stocker le rôle
        self.moteur_choisi=moteur_choisi
        self.essaiChoisi=None
        self.ui.l_axeY.setVisible(False)
        self.ui.cBoxAxeY.setVisible(False)
        self.ui.l_axeX.setVisible(False)
        self.ui.cBoxAxeX.setVisible(False)
        self.ui.pb_valider_axe.setVisible(False)
        self.ui.w_graphique.setVisible(False)
        self.layout= QVBoxLayout(self.ui.w_graphique)
        self.figure=Figure()
        self.canvas=FigureCanvas(self.figure)
        self.axes=self.figure.add_subplot(111)
        self.client=None
        self.profil_actuel = None
        self.profil_avec_temps_fixe = False
        # On ajoute le canvas au layout
        self.layout.addWidget(self.canvas)
        print(f"Utilisateur connecté : {self.identifiant}")  # Affichage en console
        # Générer une clé secrète TOTP
        self.secret = pyotp.random_base32()
        self.otp_uri = pyotp.totp.TOTP(self.secret).provisioning_uri(
            name="Double_Auth",
            issuer_name="Banc_Mot"
        )
        self.ui.tE_listeEssai.setColumnWidth(3,115)
        # Générer et afficher le QR code
        self.generate_qr_code(self.otp_uri)
        # Connecter le bouton de validation
        self.ui.pb_valider_2AF.clicked.connect(self.verifierTotp)
        self.ui.pb_deconnecter.clicked.connect(self.deconnexion)
        self.ui.pb_deconnecter_2.clicked.connect(self.deconnexion)
        self.ui.pb_deconnecter_7.clicked.connect(self.deconnexion)
        self.ui.pb_actualiser_liste_essai.clicked.connect(self.recuperer_donnee)
        self.ui.pb_trierListeEssai.clicked.connect(self.trierListe)
        self.ui.pb_selectionner_essai.clicked.connect(self.selectionnerEssai)
        self.ui.pb_piloter_frein_manuel.clicked.connect(self.piloterFreinManuel)
        self.ui.pb_piloter_frein_profil.clicked.connect(self.piloterFreinProfil)
        self.ui.pb_valider_axe.clicked.connect(self.validerAxe)
        self.ui.pb_choix_moteur.clicked.connect(self.selectionMoteur)
        self.ui.pb_ajouter_moteur.clicked.connect(self.ajouterMoteur)
        self.ui.pb_modifier_moteur.clicked.connect(self.modifierMoteur)
        self.ui.pb_supprimer_moteur.clicked.connect(self.supprimerMoteur)
        self.ui.pb_demarrer_cycle.clicked.connect(self.demarrerCycle)
        self.ui.pb_arreter_cycle.clicked.connect(self.arreterCycle)
        self.ui.pb_valider_capteur.clicked.connect(self.validerCapteur)        
        self.ui.pb_modifierCoefficient.clicked.connect(self.modifierCoeff)
        self.ui.lE_coeffCouple.setVisible(False)
        self.ui.label_9.setVisible(False)
        self.show()

    def modifierCoeff(self):
        self.ui.lE_coeffCouple.setVisible(True)
        self.ui.label_9.setVisible(True)
        self.ui.pb_modifierCoefficient.setVisible(False)
        

    def validerCapteur(self):
        coeffCourant = self.ui.cB_capteurCourant.currentText()[:-1]
        if float(coeffCourant) == 2:
            coeffCourant = 7.2
        else:
            coeffCourant = 7.2

        if self.ui.lE_coeffCouple.text()!='':
            coeffCouple = self.ui.lE_coeffCouple.text()
        else:
            coeffCouple = 25000

        try:
            if float(coeffCouple)<0:
                coeffCouple = 25000
            else:
                coeffCouple = str(coeffCouple)
        except:
            coeffCouple = 25000
        broker = "192.168.2.108"
        port = 1883
        topicCoeffCourant = "Capteur/CoeffCourant"
        topicCoeffCouple = "Capteur/CoeffCouple"
        mqtt_username = "bancmoteur"
        mqtt_password = "CestGenialCeBts2025"
        self.client = mqtt.Client()
        self.client.username_pw_set(mqtt_username, mqtt_password)
        self.client.connect(broker, port, 60)
        self.client.publish(topicCoeffCourant, coeffCourant)
        self.client.publish(topicCoeffCouple, coeffCouple) 


        
    def validerAxe(self):
        axesValeurs = {1: "tension", 2: "courant", 3: "puissance", 4: "couple", 5: "vitesse_moteur", 6: "temps"} 
        axesLabels = {"tension": "Tension (V)", "courant": "Courant (A)", "puissance": "Puissance (W)","couple": "Couple (N·m)", "vitesse_moteur": "Vitesse (tr/min)", "temps": "Temps (s)"} 
        # Dictionnaire associant un index à un nom de colonne de la BD
        self.ui.w_graphique.setVisible(True)  # Rend visible le widget contenant le graphique
        axeY = self.ui.cBoxAxeX.currentIndex()  # Récupère l'index sélectionné dans la comboBox pour l'axe Y
        axeX = self.ui.cBoxAxeY.currentIndex()  # Récupère l'index sélectionné dans la comboBox pour l'axe X
        labelY = axesValeurs.get(axeY)  # Récupère le nom de la colonne correspondant à l'axe Y
        labelX = axesValeurs.get(axeX)  # Récupère le nom de la colonne correspondant à l'axe X
        host, user, db_password, database = 'localhost', 'root', '', 'eguidat_banc_moteur'  # Paramètres de connexion à la base de données
        try:
            connection = mysql.connector.connect(host=host, user=user, password=db_password, database=database)  # Connexion à la base de données
            cursor = connection.cursor()  # Création d'un curseur pour exécuter des requêtes
            requete = f"SELECT {labelY},{labelX} FROM essai WHERE id_essai=%s"  # Requête SQL pour récupérer les deux colonnes
            cursor.execute(requete, (self.idChoisi,))  # Exécution de la requête avec l'identifiant d'essai sélectionné
            result = cursor.fetchall()  # Récupération de tous les résultats
            valeurAxeX, valeurAxeY = [], []  # Initialisation des listes pour les données X et Y
            for row in result:  # Parcours des lignes de résultat
                valeurAxeY.extend(self.convert_to_float_array(row[0]))  # Conversion et ajout des valeurs Y
                valeurAxeX.extend(self.convert_to_float_array(row[1]))  # Conversion et ajout des valeurs X
            if not valeurAxeX or not valeurAxeY:  # Vérifie si l'une des deux listes est vide
                print("Données vides, impossible de tracer le graphique.")  # Message d'erreur si données manquantes
                return  # Interrompt l'exécution de la fonction
            if len(valeurAxeX) != len(valeurAxeY):  # Vérifie la correspondance du nombre de valeurs X et Y
                print(f"Erreur : {len(valeurAxeX)} valeurs X mais {len(valeurAxeY)} valeurs Y.")  # Message d'erreur si tailles différentes
                return  # Interrompt l'exécution de la fonction
        except mysql.connector.Error as e:  # Gestion des erreurs MySQL
            print(f"Erreur MySQL : {e}")  # Affiche le message d'erreur
            return  # Interrompt l'exécution de la fonction

        for i in reversed(range(self.ui.w_graphique.layout().count())):  # Parcourt les widgets actuels du layout graphique
            self.ui.w_graphique.layout().itemAt(i).widget().deleteLater()  # Supprime chaque widget (nettoyage de l'affichage précédent)

        fig, ax = plt.subplots()  # Crée une figure et un axe pour le tracé
        ax.plot(valeurAxeX, valeurAxeY, marker="o", linestyle="None", color="b")  # Trace les points X et Y en bleu, sans ligne entre eux
        # Calcul des bornes dynamiques
        maxX = max(valeurAxeX) * 1.5
        maxY = max(valeurAxeY) * 1.5
        ax.set_xlim(left=0, right=maxX)
        ax.set_ylim(bottom=0, top=maxY)
        ax.set_xlabel(axesLabels.get(labelX,labelX))  # Ajoute un label à l'axe X
        ax.set_ylabel(axesLabels.get(labelY,labelY))  # Ajoute un label à l'axe Y
        ax.set_title(f"{axesLabels.get(labelY, labelY)} en fonction de {axesLabels.get(labelX, labelX)}")
        fig.tight_layout()  # Ajuste automatiquement les éléments pour éviter les chevauchements

        canvas = FigureCanvas(fig)  # Crée un canvas Qt pour afficher le graphique matplotlib
        layout = self.ui.w_graphique.layout()  # Récupère le layout actuel du widget graphique
        if layout is None:  # Si aucun layout n'existe encore
            layout = QVBoxLayout()  # Crée un layout vertical
            self.ui.w_graphique.setLayout(layout)  # Associe le layout au widget
        layout.addWidget(canvas)  # Ajoute le canvas contenant le graphique au layout
        canvas.draw()  # Dessine le graphique à l'écran

        
    def piloterFreinManuel(self):
        self.AppPilotage=AppPilotage(self.identifiant,self.moteur_choisi,self.role)
        self.AppPilotage.show()
        self.close()      
        
    def piloterFreinProfil(self):
        self.AppPilotageProfil=AppPilotageProfil(self.identifiant,self.moteur_choisi,self.role)
        self.AppPilotageProfil.show()
        self.close()  
        
    def demarrerCycle(self):
        broker = "192.168.2.108"
        port = 1883
        topics = ["Moteur/Ueff", "Moteur/Ieff", "Moteur/C", "Moteur/N", "Moteur/Numero"]
        topicEtatMoteur = "Moteur/Etat"
        topicNumeroMoteur = "Moteur/Numero"
        mqtt_username = "bancmoteur"
        mqtt_password = "CestGenialCeBts2025"

        # Initialisation des listes
        self.temps = []
        self.tension = []
        self.courant = []
        self.puissance = []
        self.couple = []
        self.vitesse = []

        self.nb_donnees = 0
        self.debut_cycle = None
        self.dernier_temps_mesure = None  # Pour limiter à 0.5s

        self.client = mqtt.Client()
        self.client.username_pw_set(mqtt_username, mqtt_password)
        self.client.on_message = self.on_message_received
        self.client.connect(broker, port, 60)

        for topic in topics:
            self.client.subscribe(topic)

        self.valeurs_moteur = {
            "Moteur/Ueff": None,
            "Moteur/Ieff": None,
            "Moteur/C": None,
            "Moteur/N": None,
        }

        self.client.loop_start()
        self.client.publish(topicEtatMoteur, "Marche")
        self.client.publish(topicNumeroMoteur, str(self.moteur_choisi))

    def on_message_received(self, client, userdata, message):
        try:
            topic = message.topic
            payload = message.payload.decode("utf-8")

            if topic in self.valeurs_moteur:
                self.valeurs_moteur[topic] = payload

                if all(value is not None for value in self.valeurs_moteur.values()):
                    now = time.time()

                    # Initialisation du temps de début
                    if self.debut_cycle is None:
                        self.debut_cycle = now
                        self.dernier_temps_mesure = now
                        temps_actuel = 0.0
                    else:
                        temps_actuel = round(now - self.debut_cycle, 1)

                    # Ne traiter que si au moins 0.5 seconde s’est écoulée depuis la dernière mesure
                    if now - self.dernier_temps_mesure >= 0.5 or self.nb_donnees == 0:
                        self.dernier_temps_mesure = now

                        try:
                            couple = float(self.valeurs_moteur['Moteur/C'])
                            vitesse = float(self.valeurs_moteur['Moteur/N'])
                            puissance_utile = couple * 2 * math.pi * (vitesse / 60)
                        except ValueError:
                            puissance_utile = 0.0

                        self.tension.append(self.valeurs_moteur['Moteur/Ueff'])
                        self.courant.append(self.valeurs_moteur['Moteur/Ieff'])
                        self.couple.append(self.valeurs_moteur['Moteur/C'])
                        self.vitesse.append(self.valeurs_moteur['Moteur/N'])
                        self.puissance.append(puissance_utile)
                        self.temps.append(round(temps_actuel, 1))

                        texte = (
                            f"Tension : {self.valeurs_moteur['Moteur/Ueff']}\n"
                            f"Courant : {self.valeurs_moteur['Moteur/Ieff']}\n"
                            f"Couple : {self.valeurs_moteur['Moteur/C']}\n"
                            f"Vitesse : {self.valeurs_moteur['Moteur/N']}\n"
                            f"Puissance utile : {round(puissance_utile,1)} W\n"
                            f"Temps : {temps_actuel:.1f} s\n"
                            f"-----"
                        )
                        self.ui.tE_valeur_temps_reel.append(texte)

                        self.nb_donnees += 1  # Optionnel maintenant

                    for key in self.valeurs_moteur:
                        self.valeurs_moteur[key] = None

            elif topic == "Moteur/Numero":
                self.ui.tE_valeur_temps_reel.append(f"Numéro de moteur : {payload}\n")

        except Exception as e:
            print("Erreur réception MQTT :", e)

    
        
    def arreterCycle(self):
        if self.client is not None:
            try:
                self.client.loop_stop()
                self.client.disconnect()
                self.client = None  
                self.ui.tE_valeur_temps_reel.append("Cycle arrêté.")
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
                identifiant=self.identifiant
                tension="["+";".join(self.tension)+"]"
                courant="["+";".join(self.courant)+"]"
                couple="["+";".join(self.couple)+"]"
                vitesse="["+";".join(self.vitesse)+"]"
                puissance = "[" + ";".join(str(x) for x in self.puissance) + "]"
                temps = "[" + ";".join(str(x) for x in self.temps) + "]"
                moteur_choisi=self.moteur_choisi
                requete = """INSERT INTO essai (id_essai, date_essai, identifiant_eleve_essai,tension, courant, couple, vitesse_moteur,id_moteur, puissance, temps) 
                VALUES ( NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                cursor.execute(requete,(date_essai,identifiant,tension,courant,couple,vitesse,moteur_choisi,puissance,temps))
                connection.commit()
                cursor.close()
                connection.close()
            except Exception as e:
                self.ui.tE_valeur_temps_reel.append(f"Erreur à l'arrêt du cycle : {str(e)}")
        
    def selectionnerEssai(self):
        essaiChoisi=self.ui.tE_listeEssai.currentRow()
        if essaiChoisi != -1:
            id=self.ui.tE_listeEssai.item(essaiChoisi,0)
            if id:
                self.idChoisi=id.text()
                self.ui.l_choix_essai.setText(f"Identifiant de l'essai choisi : {self.idChoisi}")
                self.ui.l_info.clear()
                self.ui.l_axeY.setVisible(True)
                self.ui.cBoxAxeY.setVisible(True)
                self.ui.l_axeX.setVisible(True)
                self.ui.cBoxAxeX.setVisible(True)
                self.ui.pb_valider_axe.setVisible(True)
                self.ui.w_graphique.setVisible(False)
                self.ui.cBoxAxeX.setCurrentIndex(0)
                self.ui.cBoxAxeY.setCurrentIndex(0)
            else : 
                self.ui.l_choix_essai.setText("Aucun essai choisi.") 

    def convert_to_float_array(self,valeur):
        # Nettoyage de la chaîne : enlever les crochets et autres caractères indésirables
        valeur_cleaned = valeur.strip('[]').replace(';', ',').replace('\r\n', '').replace(']', '')
        # Séparation de la chaîne en fonction des virgules
        valeur_list = valeur_cleaned.split(',')
        # Conversion de chaque élément de la liste en float, en filtrant les éléments vides
        try:
            float_values = [float(item) for item in valeur_list if item.strip()]  # On ignore les éléments vides
        except ValueError as e:
            print(f"Erreur de conversion de valeur : {e}")
            float_values = []
        return float_values
    
    def trierListe(self):
        # Récupère le filtre souhaité par l'utilisateur
        option_tri = self.ui.cB_listeTries.currentText()
        # Connexion à la base de donnée
        host = 'localhost'
        user = 'prof'
        db_password = 'CestGenialCeBts2025'
        database = 'eguidat_banc_moteur'
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=db_password,
                database=database
            )
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
        cursor = connection.cursor()
        # Requête initiale sans filtrage
        requete = """ 
            SELECT essai.id_essai, essai.identifiant_eleve_essai, classe.nom_classe, essai.date_essai, moteur.type
            FROM essai
            JOIN utilisateur ON essai.identifiant_eleve_essai = utilisateur.identifiant
            JOIN classe ON utilisateur.classe_id = classe.id_classe
            JOIN moteur ON essai.id_moteur = moteur.id_moteur
            """
        # Conditions pour assigner à la requête le filtre selectionné
        if option_tri == "par étudiant":
            requete += "\nORDER BY essai.identifiant_eleve_essai ASC;"
        elif option_tri == "par date":
            requete += "\nORDER BY essai.date_essai DESC;"
        elif option_tri == "par moteur":
            requete += "\nORDER BY moteur.type ASC;"
        else:
            requete += "\nORDER BY essai.id_essai ASC;"
        # Execution de la requête
        cursor.execute(requete)
        donnees = cursor.fetchall()
        # Effacer le tableau existant
        self.ui.tE_listeEssai.setRowCount(0)
        # Définir le nombre de lignes du tableau
        self.ui.tE_listeEssai.setRowCount(len(donnees))
        # Insérer les données dans le QTableWidget
        for row_idx, row_data in enumerate(donnees):
            for col_idx, value in enumerate(row_data):
                self.ui.tE_listeEssai.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        # Fermeture de la connexion SQL
        cursor.close()
        connection.close()
        self.ui.tE_listeEssai.resizeRowsToContents()
        self.ui.tE_listeEssai.setColumnWidth(0, 45)    
        # Désactive le redimensionnement automatique pour la colonne 3
        self.ui.tE_listeEssai.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        # Applique la largeur souhaitée
        self.ui.tE_listeEssai.setColumnWidth(3, 300)

    def generate_qr_code(self, uri):
        # Génère un QR code à partir de l'URI (contenant la clé secrète TOTP)
        qr = qrcode.make(uri)
        # Sauvegarde le QR code sous forme d'image PNG
        qr.save("qrcode.png")  

        # Charge l'image du QR code sous forme de QPixmap pour affichage dans l'interface
        pixmap = QPixmap("qrcode.png")
        # Vérifie si l'interface contient un label nommé "qr_label"
        if hasattr(self.ui, "qr_label"):
            # Affiche le QR code dans le label
            self.ui.qr_label.setPixmap(pixmap)
            # Adapte l’image à la taille du label
            self.ui.qr_label.setScaledContents(True)
            # Centre l’image dans le label
            self.ui.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def verifierTotp(self):
        # Récupère le code TOTP saisi par l'utilisateur
        user_input = self.ui.lE_2AF.text()
        # Crée un objet TOTP à partir de la clé secrète
        totp = pyotp.TOTP(self.secret)

        # Vérifie si le code est valide (dans la fenêtre de temps courante ou précédente)
        if totp.verify(user_input) or totp.verify(user_input, valid_window=1):
            # Affiche un message de succès
            self.ui.l_reponse.setText("Code TOTP valide")
            # Sauvegarde la clé secrète dans la base de données
            self.sauvegarder2AF()
        else:
            # Affiche un message d'erreur si le code est invalide
            self.ui.l_reponse.setText("Code TOTP invalide")

    def sauvegarder2AF(self):
        # Informations de connexion à la base de données MySQL
        host = 'localhost'
        user = 'prof'
        db_password = 'CestGenialCeBts2025'
        database = 'eguidat_banc_moteur'
        try:
            # Connexion à la base de données
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=db_password,
                database=database
            )
            # Création d'un curseur pour exécuter les requêtes SQL
            cursor = connection.cursor()
            # Requête SQL pour mettre à jour la clé secrète de l'utilisateur identifié
            requete = "UPDATE utilisateur SET secret = %s WHERE identifiant = %s"
            # Exécution de la requête avec les valeurs de la clé secrète et de l'identifiant
            cursor.execute(requete, (self.secret, self.identifiant))
            # Validation de la modification dans la base de données
            connection.commit()
            # Fermeture du curseur et de la connexion
            cursor.close()
            connection.close()
            print("Double authentification activée avec succès.")
        
        # Gestion des erreurs SQL (ex : problème de connexion, syntaxe, etc.)
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")

    
    def deconnexion(self):
        self.close()      
                
    def recuperer_donnee(self):
        host = 'localhost'
        user = 'prof'
        db_password = 'CestGenialCeBts2025'
        database = 'eguidat_banc_moteur'

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=db_password,
                database=database
            )
            cursor = connection.cursor()
            requete = """
            SELECT essai.id_essai, essai.identifiant_eleve_essai, classe.nom_classe, essai.date_essai, moteur.type, moteur.id_moteur
            FROM essai
            JOIN utilisateur ON essai.identifiant_eleve_essai = utilisateur.identifiant
            JOIN classe ON utilisateur.classe_id = classe.id_classe
            JOIN moteur ON essai.id_moteur = moteur.id_moteur;
            """
            cursor.execute(requete)
            donnees = cursor.fetchall()  # Récupérer toutes les lignes
            # Définir le nombre de lignes du tableau pour tE_listeEssai
            self.ui.tE_listeEssai.setRowCount(len(donnees))
            # Remplir la liste déroulante cBox_liste_essai
            self.ui.cBox_liste_essai.clear()  # Effacer les anciens éléments
            # Insérer les données dans le QTableWidget et QComboBox
            for row_idx, row_data in enumerate(donnees):
                # Ajouter chaque ligne au QTableWidget
                for col_idx, value in enumerate(row_data):
                    self.ui.tE_listeEssai.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
                # Ajouter une entrée dans le QComboBox
                essai_info = f"{row_data[0]} - {row_data[1]} - {row_data[4]}"
                self.ui.cBox_liste_essai.addItem(essai_info)
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
        self.ui.tE_listeEssai.resizeRowsToContents()
        self.ui.tE_listeEssai.setColumnWidth(0, 45)    
        # Désactive le redimensionnement automatique pour la colonne 3
        self.ui.tE_listeEssai.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        # Applique la largeur souhaitée
        self.ui.tE_listeEssai.setColumnWidth(3, 300)
            
    def recuperer_moteur(self):
            self.ui.tE_listeMoteur.resizeRowsToContents()
            host = 'localhost'
            user = 'prof'
            db_password = 'CestGenialCeBts2025'
            database = 'eguidat_banc_moteur'

            try:
                connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=db_password,
                    database=database
                )
                cursor = connection.cursor()
                requete = """
                SELECT id_moteur,tension,courant,couple,vitesse,puissance,type
                FROM moteur
                WHERE 1;
                """
                cursor.execute(requete)
                donnees = cursor.fetchall()  # Récupérer toutes les lignes
                # Définir le nombre de lignes du tableau pour tE_listeEssai
                self.ui.tE_listeMoteur.setRowCount(len(donnees))
                # Insérer les données dans le QTableWidget et QComboBox
                for row_idx, row_data in enumerate(donnees):
                    # Ajouter chaque ligne au QTableWidget
                    for col_idx, value in enumerate(row_data):
                        self.ui.tE_listeMoteur.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
                    # Ajouter une entrée dans le QComboBox
                    essai_info = f"{row_data[0]} - {row_data[1]} - {row_data[4]}"
                    self.ui.cBox_liste_essai.addItem(essai_info)
                cursor.close()
                connection.close()
            except mysql.connector.Error as e:
                print(f"Erreur MySQL : {e}")
                
                
    def selectionMoteur(self):
        moteur_choisi=self.ui.tE_listeMoteur.currentRow()
        if moteur_choisi != -1:
            idMoteur=self.ui.tE_listeMoteur.item(moteur_choisi,0)
            Unom=self.ui.tE_listeMoteur.item(moteur_choisi,1)
            Inom=self.ui.tE_listeMoteur.item(moteur_choisi,2)
            Cnom=self.ui.tE_listeMoteur.item(moteur_choisi,3)
            Nnom=self.ui.tE_listeMoteur.item(moteur_choisi,4)
            PUnom=self.ui.tE_listeMoteur.item(moteur_choisi,5)
            type=self.ui.tE_listeMoteur.item(moteur_choisi,6)
            if idMoteur:
                broker = "192.168.2.108"  
                port = 1883 
                topic1 = "Caracteristique/Unom"
                topic2 = "Caracteristique/Inom"
                topic3 = "Caracteristique/Cnom"
                topic4 = "Caracteristique/Nnom"
                topic5 = "Caracteristique/PUnom"
                topic6 = "Caracteristique/Type"
                mqtt_username = "bancmoteur" 
                mqtt_password = "CestGenialCeBts2025"  
                client = mqtt.Client()
                client.username_pw_set(mqtt_username, mqtt_password)
                client.connect(broker,port,60)
                client.publish(topic1,str(Unom.text()))
                client.publish(topic2,str(Inom.text()))
                client.publish(topic3,str(Cnom.text()))
                client.publish(topic4,str(Nnom.text()))
                client.publish(topic5,str(PUnom.text()))
                client.publish(topic6,str(type.text()))
                client.disconnect()
                self.moteur_choisi=idMoteur.text()
                self.ui.l_choix_moteur.setText(f"Identifiant du moteur choisi : {self.moteur_choisi}")
            else : 
                self.ui.l_choix_moteur.setText("Aucun moteur choisi.") 
        

    def ajouterMoteur(self):
        # Définir les informations de connexion à la base de données
        host = 'localhost'
        user = 'prof'
        db_password = 'CestGenialCeBts2025'
        database = 'eguidat_banc_moteur'
        try:
            # Connexion à la base de données MySQL
            connection = mysql.connector.connect(host=host, user=user, password=db_password, database=database)
            cursor = connection.cursor()
            # Récupérer le dernier id_moteur dans la base de données pour générer le nouvel id
            cursor.execute("SELECT MAX(id_moteur) FROM moteur")
            dernier_id_moteur = cursor.fetchone()
            # Si un id existe, incrémenter le dernier id, sinon commencer à 1
            if dernier_id_moteur and dernier_id_moteur[0] is not None:
                nouvel_id_moteur = dernier_id_moteur[0] + 1
            else:
                nouvel_id_moteur = 1
            # Récupérer la position actuelle des lignes dans le tableau
            row_position = self.ui.tE_listeMoteur.rowCount()
            # Ajouter une nouvelle ligne vide dans le tableau
            self.ui.tE_listeMoteur.insertRow(row_position)
            # Remplir la nouvelle ligne avec des cellules vides
            for col in range(7):
                self.ui.tE_listeMoteur.setItem(row_position, col, QTableWidgetItem(""))
            # Ajouter l'id_moteur généré dans la première colonne de la nouvelle ligne
            self.ui.tE_listeMoteur.setItem(row_position, 0, QTableWidgetItem(str(nouvel_id_moteur)))
            # Connecter le signal cellChanged à la fonction on_cell_changed
            self.ui.tE_listeMoteur.cellChanged.connect(self.on_cell_changed)
        except mysql.connector.Error as e:
            # En cas d'erreur de connexion à MySQL, afficher l'erreur
            print(f"Erreur MySQL : {e}")

    def on_cell_changed(self, row, column):
        host = 'localhost'
        user = 'prof'
        db_password = 'CestGenialCeBts2025'
        database = 'eguidat_banc_moteur'
        if column == 6:  # Assure-toi que c'est la dernière colonne qui déclenche l'action
            valeur = [self.ui.tE_listeMoteur.item(row, i).text() for i in range(1, 7)]  # Récupère les valeurs des cellules
            if all(valeur):  # Vérifie que toutes les cellules sont remplies
                try:
                    # Si 'id_moteur' est auto-incrémenté, on ne doit pas l'inclure dans la requête
                    id_moteur = self.ui.tE_listeMoteur.item(row, 0).text()  # Récupère l'ID du moteur
                    if not id_moteur:  # Si l'ID est vide, il ne faut pas insérer une ligne
                        self.ui.l_choix_moteur.setText("Erreur : ID du moteur vide")
                        return
                    
                    connection = mysql.connector.connect(host=host, user=user, password=db_password, database=database)
                    cursor = connection.cursor()

                    # Requête d'insertion
                    requete = """INSERT INTO moteur (id_moteur, tension, courant, couple, vitesse, puissance, type)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    
                    cursor.execute(requete, [id_moteur] + valeur)
                    connection.commit()

                    # Retour après insertion
                    self.ui.l_choix_moteur.setText("Moteur bien ajouté")
                    
                except mysql.connector.Error as e:
                    self.ui.l_choix_moteur.setText(f"Erreur d'insertion : {e}")
                finally:
                    # Toujours fermer la connexion et le curseur
                    cursor.close()
                    connection.close()

    def modifierMoteur(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='prof',
                password='CestGenialCeBts2025',
                database='eguidat_banc_moteur'
            )
            cursor = connection.cursor()

            row = self.ui.tE_listeMoteur.currentRow()
            if row == -1:
                self.ui.l_choix_moteur.setText("Veuillez sélectionner un moteur.")
                return

            id_moteur = self.ui.tE_listeMoteur.item(row, 0).text()
            tension = self.ui.tE_listeMoteur.item(row, 1).text()
            courant = self.ui.tE_listeMoteur.item(row, 2).text()
            couple = self.ui.tE_listeMoteur.item(row, 3).text()
            vitesse = self.ui.tE_listeMoteur.item(row, 4).text()
            puissance = self.ui.tE_listeMoteur.item(row, 5).text()
            type_moteur = self.ui.tE_listeMoteur.item(row, 6).text()

            requete = """UPDATE moteur
                        SET tension=%s, courant=%s, couple=%s, vitesse=%s, puissance=%s, type=%s 
                        WHERE id_moteur=%s"""
            cursor.execute(requete, (tension, courant, couple, vitesse, puissance, type_moteur, id_moteur))
            connection.commit()
            connection.close()

            self.ui.l_choix_moteur.setText("Moteur modifié avec succès")
        except Exception as e:
            print(e)
            self.ui.l_choix_moteur.setText("Erreur lors de la modification")
            
            
    def supprimerMoteur(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='prof',
                password='CestGenialCeBts2025',
                database='eguidat_banc_moteur'
            )
            cursor = connection.cursor()
            row = self.ui.tE_listeMoteur.currentRow()
            if row == -1:
                self.ui.l_choix_moteur.setText("Veuillez sélectionner un moteur à supprimer.")
                return
            id_moteur = self.ui.tE_listeMoteur.item(row, 0).text()
            requete = """DELETE FROM moteur WHERE id_moteur=%s"""
            cursor.execute(requete, (id_moteur,))
            connection.commit()
            self.ui.tE_listeMoteur.removeRow(row)
            connection.close()
            self.ui.l_choix_moteur.setText("Moteur supprimé avec succès")
        except Exception as e:
            print(e)
            self.ui.l_choix_moteur.setText("Erreur lors de la suppression")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    identifiant = "utilisateur_exemple"  # Remplacez ceci par un identifiant valide
    window = AppBancMot(identifiant)  # Utilisez AppBancMot pour afficher l'interface
    sys.exit(app.exec())