import sys
import qrcode
import pyotp  
import mysql.connector
import bcrypt
from datetime import datetime
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem, QComboBox, QLineEdit, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt 
from accueil_prof import Ui_AppBancMot_prof  
from app_choix_moteur import AppChoixMoteur
from app_pilotage import AppPilotage
from App_pilotage_frein_profil import AppPilotageProfil

class AppBancMotProf(QWidget):
    def __init__(self, identifiant,moteur_choisi=None):
        super().__init__()
        self.ui = Ui_AppBancMot_prof()  
        self.ui.setupUi(self)  # Configure l'interface
        self.showFullScreen()
        self.recuperer_donnee()
        self.recuperer_utilisateur()
        self.recuperer_moteur()
        self.recuperer_capteur()
        self.essaiSelectionne=None
        self.identifiant=identifiant  # Stocker l'identifiant
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
        self.ui.pb_valider_2AF.clicked.connect(self.verify_totp)
        self.ui.pb_deconnecter.clicked.connect(self.deconnexion)
        self.ui.pb_deconnecter_2.clicked.connect(self.deconnexion)
        self.ui.pb_deconnecter_5.clicked.connect(self.deconnexion)
        self.ui.pb_deconnecter_6.clicked.connect(self.deconnexion)
        self.ui.pb_deconnecter_7.clicked.connect(self.deconnexion)
        self.ui.pb_actualiser_liste_essai.clicked.connect(self.recuperer_donnee)
        self.ui.pb_trierListeEssai.clicked.connect(self.trierListe)
        self.ui.pb_selectionner_essai.clicked.connect(self.selectionnerEssai)
        self.ui.pb_valider_ajout_eleve.clicked.connect(self.ajouterEleve)
        self.ui.pb_choix_fichierCSV.clicked.connect(self.choixFichierEleve)
        self.ui.pb_piloter_frein_manuel.clicked.connect(self.piloterFreinManuel)
        self.ui.pb_piloter_frein_profil.clicked.connect(self.piloterFreinProfil)
        self.ui.pb_generer_caracteristique.clicked.connect(self.genererCaracteristique)
        self.ui.pb_valider_axe.clicked.connect(self.validerAxe)
        self.ui.pb_choix_moteur.clicked.connect(self.selectionMoteur)
        self.ui.pb_ajouter_moteur.clicked.connect(self.ajouterMoteur)
        self.ui.pb_modifier_moteur.clicked.connect(self.modifierMoteur)
        self.ui.pb_supprimer_moteur.clicked.connect(self.supprimerMoteur)
        self.ui.pb_demarrer_cycle.clicked.connect(self.demarrerCycle)
        self.ui.pb_arreter_cycle.clicked.connect(self.arreterCycle)
        "self.ui.pb_valider_ajout_eleve_csv.connect(self.ajouterEleveCsv)"
        self.show()
        
    def validerAxe(self):
        axesValeurs = {1:"tension", 2:"courant", 3:"puissance", 4:"couple", 5:"vitesse_moteur"}
        self.ui.w_graphique.setVisible(True)

        axeY = self.ui.cBoxAxeX.currentIndex()
        axeX = self.ui.cBoxAxeY.currentIndex()
        labelY = axesValeurs.get(axeY)
        labelX = axesValeurs.get(axeX)

        host, user, db_password, database = 'localhost', 'root', '', 'eguidat_banc_moteur'

        try:
            connection = mysql.connector.connect(host=host, user=user, password=db_password, database=database)
            cursor = connection.cursor()
            requete = f"SELECT temps,{labelY},{labelX} FROM essai WHERE id_essai=%s"
            cursor.execute(requete, (self.idChoisi,))
            result = cursor.fetchall()

            valeurAxeX, valeurAxeY = [], []
            for row in result:
                valeurAxeY.extend(self.convert_to_float_array(row[1]))
                valeurAxeX.extend(self.convert_to_float_array(row[2]))

            if not valeurAxeX or not valeurAxeY:
                print("Données vides, impossible de tracer le graphique.")
                return
            if len(valeurAxeX) != len(valeurAxeY):
                print(f"Erreur : {len(valeurAxeX)} valeurs X mais {len(valeurAxeY)} valeurs Y.")
                return

        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
            return

        for i in reversed(range(self.ui.w_graphique.layout().count())):
            self.ui.w_graphique.layout().itemAt(i).widget().deleteLater()

        fig, ax = plt.subplots()
        ax.plot(valeurAxeX, valeurAxeY, marker="o", linestyle="-", color="b")
        ax.set_xlabel(labelX)
        ax.set_ylabel(labelY)
        ax.set_title(f"Graphique de {labelY} en fonction de {labelX}")
        fig.tight_layout()

        canvas = FigureCanvas(fig)
        layout = self.ui.w_graphique.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.w_graphique.setLayout(layout)
        layout.addWidget(canvas)
        canvas.draw()

    
    def genererCaracteristique(self):
        self.ui.l_axeY.setVisible(True)
        self.ui.cBoxAxeY.setVisible(True)
        self.ui.l_axeX.setVisible(True)
        self.ui.cBoxAxeX.setVisible(True)
        self.ui.pb_valider_axe.setVisible(True)
        
    def piloterFreinManuel(self):
        self.AppPilotage=AppPilotage(self.identifiant)
        self.AppPilotage.show()
        self.close()      
        
    def piloterFreinProfil(self):
        self.AppPilotageProfil=AppPilotageProfil(self.identifiant, self.moteur_choisi)
        self.AppPilotageProfil.show()
        self.close()  
        
    def demarrerCycle(self):
        broker = "192.168.2.100"
        port = 1883
        topics = ["Moteur/Ueff", "Moteur/Ieff", "Moteur/C", "Moteur/N", "Moteur/Numero"]
        topicEtatMoteur = "Moteur/Etat"
        topicNumeroMoteur = "Moteur/Numero"
        mqtt_username = "bancmoteur"
        mqtt_password = "CestGenialCeBts2025"
        self.temps=[]
        self.tension=[]
        self.courant=[]
        self.couple=[]
        self.vitesse=[]
        self.client = mqtt.Client()
        self.client.username_pw_set(mqtt_username, mqtt_password)
        self.client.on_message = self.on_message_received
        self.client.connect(broker, port, 60)
        for topic in topics:
            self.client.subscribe(topic)
        # Dictionnaire pour stocker les valeurs reçues
        self.valeurs_moteur = {
            "Moteur/Ueff": None,
            "Moteur/Ieff": None,
            "Moteur/C": None,
            "Moteur/N": None
        }
        self.client.loop_start()
        # Publier les informations initiales
        self.client.publish(topicEtatMoteur, "Marche")
        self.client.publish(topicNumeroMoteur, str(self.moteur_choisi))  # Envoie du numéro de moteur

  

    def on_message_received(self, client, userdata, message):
        try:
            topic = message.topic
            payload = message.payload.decode("utf-8")

            if topic in self.valeurs_moteur:
                self.valeurs_moteur[topic] = payload

                # Vérifie si toutes les valeurs sont présentes
                if all(value is not None for value in self.valeurs_moteur.values()):
                    texte = (
                        f"Tension : {self.valeurs_moteur['Moteur/Ueff']}\n"
                        f"Courant : {self.valeurs_moteur['Moteur/Ieff']}\n"
                        f"Couple : {self.valeurs_moteur['Moteur/C']}\n"
                        f"Vitesse : {self.valeurs_moteur['Moteur/N']}\n"
                        f"-----"
                    )
                    self.ui.tE_valeur_temps_reel.append(texte)
                    self.tension.append(self.valeurs_moteur['Moteur/Ueff'])
                    self.courant.append(self.valeurs_moteur['Moteur/Ieff'])
                    self.couple.append(self.valeurs_moteur['Moteur/C'])
                    self.vitesse.append(self.valeurs_moteur['Moteur/N'])
                    # Réinitialise les valeurs pour attendre un nouveau lot
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
                user = 'root'
                db_password = ''
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
                vitesse_moteur="["+";".join(self.vitesse)+"]"
                moteur_choisi=self.moteur_choisi
                requete = """INSERT INTO essai (id_essai, date_essai, identifiant_eleve_essai,tension, courant, couple, vitesse_moteur,id_moteur, puissance, temps) 
                VALUES ( NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                cursor.execute(requete,(date_essai,identifiant,tension,courant,couple,vitesse_moteur,moteur_choisi,str(0),str(0)))
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
                self.ui.l_tension.setText("Tension :")
                self.ui.l_courant.setText("Courant : ")
                self.ui.l_puissance.setText("Puissance : ")
                self.ui.l_couple.setText("Couple : ")
                self.ui.l_vitesse.setText("Vitesse : ")
                self.ui.l_info.clear()
                self.ui.l_axeY.setVisible(False)
                self.ui.cBoxAxeY.setVisible(False)
                self.ui.l_axeX.setVisible(False)
                self.ui.cBoxAxeX.setVisible(False)
                self.ui.pb_valider_axe.setVisible(False)
                self.ui.w_graphique.setVisible(False)
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
        user = 'root'
        db_password = ''
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

    def generate_qr_code(self, uri):
        qr = qrcode.make(uri)
        qr.save("qrcode.png")  

        pixmap = QPixmap("qrcode.png")
        if hasattr(self.ui, "qr_label"):
            self.ui.qr_label.setPixmap(pixmap)
            self.ui.qr_label.setScaledContents(True)
            self.ui.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def verify_totp(self):
        user_input = self.ui.lE_2AF.text()
        totp = pyotp.TOTP(self.secret)

        if totp.verify(user_input) or totp.verify(user_input, valid_window=1):
            self.ui.l_reponse.setText("Code TOTP valide")
            self.save_secret_to_db()
        else:
            self.ui.l_reponse.setText("Code TOTP invalide")

    def save_secret_to_db(self):
        host = 'localhost'
        user = 'root'
        db_password = ''
        database = 'eguidat_banc_moteur'

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=db_password,
                database=database
            )
            cursor = connection.cursor()

            requete = "UPDATE utilisateur SET secret = %s WHERE identifiant = %s"
            cursor.execute(requete, (self.secret, self.identifiant))
            connection.commit()

            cursor.close()
            connection.close()
            print("Clé secrète enregistrée avec succès.")
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
    
    def deconnexion(self):
        self.close()
    
    def ajouterEleve(self):
        nom=self.ui.lE_nom_eleve.text().strip()
        prenom=self.ui.lE_prenom_eleve.text().strip()
        classe=self.ui.lE_classe_eleve.text()
        identifiant=prenom[0].lower()+nom.lower()
        host = 'localhost'
        user = 'root'
        db_password = ''
        database = 'eguidat_banc_moteur'
        try:
            connection = mysql.connector.connect(
                host=host,user=user,password=db_password,database=database
            )
            cursor = connection.cursor(dictionary=True)
            requete_identifiant="SELECT identifiant FROM utilisateur WHERE identifiant=%s;"
            cursor.execute(requete_identifiant,(identifiant,))
            resultat_identifiant = cursor.fetchone()
            if resultat_identifiant is None : 
                requete_classe="SELECT nom_classe, id_classe FROM classe WHERE nom_classe=%s;"
                cursor.execute(requete_classe,(classe,))
                resultat_classe=cursor.fetchone()
                cursor.fetchall()
                if resultat_classe is None :
                    requete_ajout_classe = "INSERT INTO classe(nom_classe) VALUES(%s);"
                    cursor.execute(requete_ajout_classe,(classe,))
                    connection.commit()  
                    # Récupérer l'ID de la classe après insertion
                    requete_choix_classe = "SELECT id_classe FROM classe WHERE nom_classe=%s;"
                    cursor.execute(requete_choix_classe,(classe,))
                    id_classe = cursor.fetchone()['id_classe']  # Récupérer l'id de la classe
                else:
                    # La classe existe déjà, récupérer l'ID
                    id_classe = resultat_classe['id_classe']
                # Ajouter l'élève
                requete_ajout_eleve = "INSERT INTO utilisateur (identifiant, role, classe_id, nom, prenom) VALUES (%s,'eleve',%s, %s, %s);"
                cursor.execute(requete_ajout_eleve,(identifiant,id_classe,nom,prenom))
                connection.commit()
                self.ui.l_resultat_ajout_eleve.setText("Élève ajouté avec succès.")
            else:
                self.ui.l_resultat_ajout_eleve.setText("Erreur Identifiant, l'identifiant existe déjà !")
            self.recuperer_utilisateur()
            
            
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
            
    def choixFichierEleve(self):
        # Utiliser QFileDialog pour choisir un fichier
        fichierCsv, _ = QFileDialog.getOpenFileName(self, "Choisir un fichier", "", "Tous les fichiers (*)")

        if fichierCsv:
            nomFichier=fichierCsv.split("/")[-1] 
            self.ui.l_nomFichier.setText("Fichier ouvert : " + nomFichier)
        else:
            self.ui.l_nomFichier.setText("Aucun fichier ouvert")
            
    def recuperer_donnee(self):
        host = 'localhost'
        user = 'root'
        db_password = ''
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
            
    def recuperer_utilisateur(self):
        host = 'localhost'
        user = 'root'
        db_password = ''
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
            SELECT utilisateur.identifiant, utilisateur.role, classe.nom_classe,utilisateur.nom, utilisateur.prenom
            FROM classe,utilisateur
            WHERE utilisateur.classe_id=classe.id_classe;
            """
            cursor.execute(requete)
            donnees = cursor.fetchall()  # Récupérer toutes les lignes
            # Définir le nombre de lignes du tableau pour tE_listeEssai
            self.ui.tE_listeUtilisateur.setRowCount(len(donnees))
            # Remplir la liste déroulante cBox_liste_essai
            #self.ui.cBox_liste_essai.clear()  #é Effacer les anciens éléments
            # Insérer les données dans le QTableWidget et QComboBox
            for row_idx, row_data in enumerate(donnees):
                # Ajouter chaque ligne au QTableWidget
                for col_idx, value in enumerate(row_data):
                    self.ui.tE_listeUtilisateur.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
            
    def recuperer_moteur(self):
            host = 'localhost'
            user = 'root'
            db_password = ''
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
                
    def recuperer_capteur(self):
            host = 'localhost'
            user = 'root'
            db_password = ''
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
                SELECT id_capteur,grandeurs,valeur,nom_capteur
                FROM parametres_capteurs
                WHERE 1;
                """
                cursor.execute(requete)
                donnees = cursor.fetchall()  # Récupérer toutes les lignes
                # Définir le nombre de lignes du tableau pour tE_listeEssai
                self.ui.tE_listeCapteur.setRowCount(len(donnees))
                # Remplir la liste déroulante cBox_liste_essai
                #self.ui.cBox_liste_essai.clear()  #é Effacer les anciens éléments
                # Insérer les données dans le QTableWidget et QComboBox
                for row_idx, row_data in enumerate(donnees):
                    # Ajouter chaque ligne au QTableWidget
                    for col_idx, value in enumerate(row_data):
                        self.ui.tE_listeCapteur.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
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
                broker = "192.168.2.100"  
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
        user = 'root'
        db_password = ''
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
        user = 'root'
        db_password = ''
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
                user='root',
                password='',
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
                user='root',
                password='',
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
    window = AppBancMotProf(identifiant)  # Utilisez AppBancMot pour afficher l'interface
    sys.exit(app.exec())
