import sys
import qrcode
import pyotp  
import mysql.connector
import bcrypt
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem, QComboBox, QLineEdit, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from accueil_prof import Ui_AppBancMot_prof  
from app_choix_moteur import AppChoixMoteur
from app_pilotage import AppPilotage

class AppBancMotProf(QWidget):
    def __init__(self, identifiant,moteur_choisi=None):
        super().__init__()
        self.ui = Ui_AppBancMot_prof()  
        self.ui.setupUi(self)  # Configure l'interface
        self.showFullScreen()
        self.recuperer_donnee()
        self.ui.lE_mdp_eleve.setEchoMode(QLineEdit.Password)
        self.essaiSelectionne=None
        self.identifiant=identifiant  # Stocker l'identifiant
        self.moteur_choisi=moteur_choisi
        self.essaiChoisi=None
        self.ui.l_axeY.setVisible(False)
        self.ui.cBoxAxeY.setVisible(False)
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
        # Modification de la largeur des colonnes de la liste des essais
        self.ui.tE_listeEssai.setColumnWidth(0, 25)
        self.ui.tE_listeEssai.setColumnWidth(1, 75)
        self.ui.tE_listeEssai.setColumnWidth(2, 75)
        self.ui.tE_listeEssai.setColumnWidth(3, 115)
        self.ui.tE_listeEssai.setColumnWidth(4,75)
        # Générer et afficher le QR code
        self.generate_qr_code(self.otp_uri)
        # Connecter le bouton de validation
        self.ui.pb_valider_2AF.clicked.connect(self.verify_totp)
        self.ui.pb_choisir_moteur.clicked.connect(self.choisirMoteur)
        self.ui.pb_deconnecter.clicked.connect(self.deconnexion)
        self.ui.pb_actualiser_liste_essai.clicked.connect(self.recuperer_donnee)
        self.ui.pb_trierListeEssai.clicked.connect(self.trierListe)
        self.ui.pb_selectionner_essai.clicked.connect(self.selectionnerEssai)
        self.ui.pb_valider_ajout_eleve.clicked.connect(self.ajouterEleve)
        self.ui.pb_choix_fichierCSV.clicked.connect(self.choixFichierEleve)
        self.ui.pb_piloter_frein_manuel.clicked.connect(self.piloterFreinManuel)
        self.ui.pb_visualiser_grandeurs.clicked.connect(self.visualiserGrandeurs)
        self.ui.pb_generer_caracteristique.clicked.connect(self.genererCaracteristique)
        self.ui.pb_valider_axe.clicked.connect(self.validerAxe)
        "self.ui.pb_valider_ajout_eleve_csv.connect(self.ajouterEleveCsv)"
        match moteur_choisi:
            case None:
                self.ui.l_moteur.setText("Aucun moteur choisi")
            case 1:
                self.ui.l_moteur.setText("Moteur asynchrone 300 W (MAS) choisi")
            case 2:
                self.ui.l_moteur.setText("Moteur asynchrone 1.5 kW (MAS) choisi")
            case 3:
                self.ui.l_moteur.setText("Moteur à courant continu 0.18 kW (Mcc) choisi")
            case 4:
                self.ui.l_moteur.setText("Moteur à courant continu 0.46 kW (Mcc) choisi")
            case 5:
                self.ui.l_moteur.setText("Moteur à courant continu 0.7 kW (Mcc) choisi")
            case 6:
                self.ui.l_moteur.setText("Moteur à courant continu 0.85 kW (Mcc) choisi")
            case 7:
                self.ui.l_moteur.setText("Moteur à courant continu 1.15 kW (Mcc) choisi")
            case 8:
                self.ui.l_moteur.setText("Moteur à courant continu 1.5 kW (Mcc) choisi")
        self.show()
        
    def validerAxe(self):
        # Dictionnaire associant un index à un type de mesure
        axesValeurs = {1:"tension",2:"courant",3:"puissance",4:"couple",5:"vitesse_moteur"}
        self.ui.w_graphique.setVisible(True)  # Affichage du widget graphique
        # Récupération de l'index sélectionné et de l'étiquette correspondante
        axeY = self.ui.cBoxAxeY.currentIndex()
        labelY = axesValeurs.get(axeY)
        # Paramètres de connexion à la base de données
        host, user, db_password, database = 'localhost', 'root', '', 'eguidat_banc_moteur'
        try:
            # Connexion à la base de données MySQL et exécution de la requête
            connection = mysql.connector.connect(host=host, user=user, password=db_password, database=database)
            cursor = connection.cursor()
            requete = f"SELECT temps,{labelY} FROM essai WHERE id_essai=%s"
            cursor.execute(requete, (self.idChoisi,))
            result = cursor.fetchall()
            # Initialisation des listes pour stocker les données des axes X et Y
            valeurAxeX, valeurAxeY = [], []
            for row in result:
                valeurAxeX.extend(self.convert_to_float_array(row[0]))
                valeurAxeY.extend(self.convert_to_float_array(row[1]))
            # Vérification de la présence de données avant de tracer le graphique
            if not valeurAxeX or not valeurAxeY:
                print("Données vides, impossible de tracer le graphique.")
                return
        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
            return
        # Suppression des anciens widgets affichés dans le graphique
        for i in reversed(range(self.ui.w_graphique.layout().count())):
            self.ui.w_graphique.layout().itemAt(i).widget().deleteLater()
        # Affichage des tailles des listes pour le débogage
        print("Taille de valeurAxeX:", len(valeurAxeX))
        print("Taille de valeurAxeY:", len(valeurAxeY))
        # Création et affichage du graphique
        fig, ax = plt.subplots()
        ax.plot(valeurAxeX, valeurAxeY, marker="o", linestyle="-", color="b")
        ax.set_xlabel("Temps en s")
        ax.set_ylabel(labelY)
        ax.set_title(f"Graphique de {labelY} en fonction du temps")
        fig.tight_layout()
        # Ajout du graphique à l'interface
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
        self.ui.pb_valider_axe.setVisible(True)
        
    def piloterFreinManuel(self):
        self.AppPilotage=AppPilotage(self.identifiant)
        self.show()
        self.close()        
        
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


    def visualiserGrandeurs(self):
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
            requete = "SELECT tension,courant,couple,vitesse_moteur,puissance FROM essai WHERE id_essai=%s"
            cursor.execute(requete, (self.idChoisi,))
            result=cursor.fetchall()
            tension=[]
            courant=[]
            couple=[]
            vitesse_moteur=[]
            puissance=[]
            for row in result:
                tension=self.convert_to_float_array(row[0])
                courant=self.convert_to_float_array(row[1])
                couple=self.convert_to_float_array(row[2])
                vitesse_moteur=self.convert_to_float_array(row[3])
                puissance=self.convert_to_float_array(row[4])
            moyenneTension=round(sum(tension)/len(tension),2)
            moyenneCourant=round(sum(courant)/len(courant),2)
            moyenneCouple=round(sum(couple)/len(couple),2)
            moyenneVitesse_moteur=round(sum(vitesse_moteur)/len(vitesse_moteur),2)
            moyennePuissance=round(sum(puissance)/len(puissance),2)
            self.ui.l_tension.setText(f"Tension : {moyenneTension} V")
            self.ui.l_courant.setText(f"Courant : {moyenneCourant} A")
            self.ui.l_couple.setText(f"Couple : {moyenneCouple} N/m")
            self.ui.l_vitesse.setText(f"Vitesse : {moyenneVitesse_moteur} tr/min")
            self.ui.l_puissance.setText(f"Puissance : {moyennePuissance} W")
            self.ui.l_info.setText("Moyenne des grandeurs électriques et mécaniques :")

        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
    
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

    def choisirMoteur(self):
        print("Bouton cliqué, lancement de AppChoixMoteur")  # Debug
        self.choixMoteur = AppChoixMoteur(self.identifiant)
        print("Fenêtre créée, affichage en cours...")  # Debug
        self.choixMoteur.show()
        self.close()  # Pour cacher au lieu de fermer
    
    def ajouterEleve(self):
        nom=self.ui.lE_nom_eleve.text()
        prenom=self.ui.lE_prenom_eleve.text()
        classe=self.ui.lE_classe_eleve.text()
        identifiant=self.ui.lE_identifiant_eleve.text()
        mdp=self.ui.lE_mdp_eleve.text()
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
                requete_classe="SELECT nom_classe FROM classe WHERE nom_classe=%s;"
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
                mdp=bcrypt.hashpw(mdp.encode(),bcrypt.gensalt()).decode()
                # Ajouter l'élève
                requete_ajout_eleve = "INSERT INTO utilisateur (identifiant, mdp, role, classe_id, nom, prenom) VALUES (%s, %s, 'eleve', %s, %s, %s);"
                cursor.execute(requete_ajout_eleve,(identifiant,mdp,id_classe,nom,prenom))
                connection.commit()
                self.ui.l_resultat_ajout_eleve.setText("Élève ajouté avec succès.")
            else:
                self.ui.l_resultat_ajout_eleve.setText("Erreur Identifiant, l'identifiant existe déjà !")
            
            
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
            SELECT essai.id_essai, essai.identifiant_eleve_essai, classe.nom_classe, essai.date_essai, moteur.type
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
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    identifiant = "utilisateur_exemple"  # Remplacez ceci par un identifiant valide
    window = AppBancMotProf(identifiant)  # Utilisez AppBancMot pour afficher l'interface
    sys.exit(app.exec())
