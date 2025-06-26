import sys
import mysql.connector  # Connexion à la base de données MySQL
import bcrypt  # Pour le hachage et la vérification des mots de passe
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QMainWindow
from PyQt6.QtCore import Qt
from authentifier import Ui_Connexion  # Interface de connexion
from C2AF import Double_Auth  # Interface pour la double authentification
from CAccueil import AppBancMot  # Interface principale pour un élève
from CAccueil_prof import AppBancMotProf  # Interface principale pour un professeur

class Connexion(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Connexion()
        self.ui.setupUi(self)
        self.center()
        # Connecte le bouton à la fonction d'authentification
        self.ui.pb_connecter.clicked.connect(self.authentifier)
        # Cache le mot de passe saisi
        self.ui.le_mdp.setEchoMode(QLineEdit.EchoMode.Password)
        # Variables pour gérer un éventuel changement de mot de passe
        self.en_changement_mdp = False
        self.identifiant_a_changer = None
        self.role = None

    def center(self):
        # Récupère la géométrie de la fenêtre
        qr = self.frameGeometry()
        # Récupère le centre de l'écran principal
        screen = QApplication.primaryScreen()
        screen_center = screen.availableGeometry().center()
        # Replace la fenêtre autour du centre de l'écran
        qr.moveCenter(screen_center)
        self.move(qr.topLeft())
 
    def authentifier(self):
        identifiant = self.ui.le_identifiant.text()
        mdp = self.ui.le_mdp.text()
        # Si on est en mode "changement de mot de passe"
        if self.en_changement_mdp:
            identifiant = self.identifiant_a_changer
            if mdp == "":
                self.ui.l_erreur.setText("Veuillez remplir le champ du mot de passe.")
                return
            if mdp == "changeme" or len(mdp) < 6:
                self.ui.l_erreur.setText("Veuillez saisir un nouveau mot de passe valide \n(différent de 'changeme', min 6 caractères).")
                return
            self.changer_mot_de_passe(identifiant, mdp)
            return

        # Si des champs sont vides
        if identifiant == "" and mdp == "":
            self.ui.l_erreur.setText("Veuillez remplir tous les champs.")
            return

        # Connexion à la base de données
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='prof',
                password='CestGenialCeBts2025',
                database='eguidat_banc_moteur'
            )
            cursor = connection.cursor(dictionary=True)

            # On récupère l'utilisateur correspondant à l'identifiant
            cursor.execute("SELECT mdp, premiere_connexion, role, secret FROM utilisateur WHERE identifiant = %s", (identifiant,))
            result = cursor.fetchone()

            if result is None:
                self.ui.l_erreur.setText("Identifiant ou mot de passe incorrect.")
            else:
                hashed_password = result["mdp"]
                premiere_connexion = result["premiere_connexion"]
                role = result["role"]
                print(role)
                # Vérification du mot de passe avec bcrypt
                if bcrypt.checkpw(mdp.encode(), hashed_password.encode()):

                    # Si c’est la première connexion avec mot de passe "changeme"
                    if premiere_connexion is None or premiere_connexion==0 and mdp == "changeme":
                        self.ui.l_erreur.setText(
                            "Première connexion détectée.\nVeuillez entrer un nouveau mot de passe différent de 'changeme' puis cliquez à nouveau."
                        )
                        self.en_changement_mdp = True
                        self.identifiant_a_changer = identifiant
                        return

                    # Si la double authentification est activée
                    if result["secret"]:
                        self.Double_Authentification = Double_Auth(identifiant, role)
                        self.Double_Authentification.show()
                        self.close()
                    else:
                        # Lancement de l’interface selon le rôle
                        if result["role"] == "prof":
                            self.accueil = AppBancMotProf(identifiant, role)
                        else:
                            self.accueil = AppBancMot(identifiant,role)
                        self.ui.le_mdp.clear()
                        self.ui.le_identifiant.clear()
                        self.accueil.show()
                        self.close()
                else:
                    self.ui.l_erreur.setText("Identifiant ou mot de passe incorrect.")

            cursor.close()
            connection.close() 

        except mysql.connector.Error as e:
            self.ui.l_erreur.setText(f"Problème de connexion à la base de données : {e}")

    def changer_mot_de_passe(self, identifiant, nouveau_mdp):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='prof',
                password='CestGenialCeBts2025',
                database='eguidat_banc_moteur'
            )
            cursor = connection.cursor()

            # Hachage du nouveau mot de passe
            nouveau_hash = bcrypt.hashpw(nouveau_mdp.encode(), bcrypt.gensalt()).decode()

            # Mise à jour dans la base avec la date de première connexion
            cursor.execute(
                "UPDATE utilisateur SET mdp = %s, premiere_connexion = NOW() WHERE identifiant = %s",
                (nouveau_hash, identifiant)
            )
            connection.commit()
            cursor.close()
            connection.close()

            # Message de succès et réinitialisation des champs
            self.ui.l_erreur.setText("Mot de passe changé avec succès.\nVeuillez vous reconnecter.")
            self.en_changement_mdp = False
            self.identifiant_a_changer = None
            self.ui.le_identifiant.clear()
            self.ui.le_mdp.clear()

        except mysql.connector.Error as e:
            self.ui.l_erreur.setText(f"Erreur lors du changement de mot de passe : {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Connexion()  
    fenetre.show()
    sys.exit(app.exec())
