import sys
import qrcode
import pyotp  
import mysql.connector
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget
from accueil_prof import Ui_AppBancMot_prof  
from app_choix_moteur import AppChoixMoteur

class AppBancMotProf(QWidget):
    def __init__(self, identifiant):
        super().__init__()
        self.ui = Ui_AppBancMot_prof()
        self.ui.setupUi(self)  # Configure l'interface
        self.showFullScreen()
        self.identifiant = identifiant  # Stocker l'identifiant
        print(f"Utilisateur connecté : {self.identifiant}")  # Affichage en console

        # Générer une clé secrète TOTP
        self.secret = pyotp.random_base32()
        self.otp_uri = pyotp.totp.TOTP(self.secret).provisioning_uri(
            name="Double_Auth",
            issuer_name="Banc_Mot"
        )

        # Générer et afficher le QR code
        self.generate_qr_code(self.otp_uri)

        # Connecter le bouton de validation
        self.ui.pb_valider_2AF.clicked.connect(self.verify_totp)
        self.ui.pb_choisir_moteur.clicked.connect(self.choisirMoteur)
        self.ui.pb_deconnexion.clicked.connect(self.deconnexion)
        self.show()

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
        host = 'mysql-eguidat.alwaysdata.net'
        user = 'eguidat_banc_mot'
        db_password = 'CestGénialCeBts2025*!'
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
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    identifiant = "utilisateur_exemple"  # Remplacez ceci par un identifiant valide
    window = AppBancMotProf(identifiant)  # Utilisez AppBancMot pour afficher l'interface
    sys.exit(app.exec())
