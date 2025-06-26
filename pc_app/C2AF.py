from double_authentification_ui import Ui_Double_Auth
import mysql.connector
import bcrypt
import pyotp
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from authentifier import Ui_Connexion
from CAccueil import AppBancMot  
from CAccueil_prof import AppBancMotProf

class Double_Auth(QWidget):
    def __init__(self,identifiant,role):
        super().__init__()
        self.ui = Ui_Double_Auth()
        self.identifiant = identifiant
        self.role=role
        print(f"Utilisateur connecté : {self.identifiant}")  # Affichage en console
        self.center()
        self.ui.setupUi(self)
        self.ui.pb_envoyer_code2AF.clicked.connect(self.valider2AF)
        self.show()
        
    def center(self):
        # Récupère la géométrie de la fenêtre
        qr = self.frameGeometry()
        # Récupère le centre de l'écran principal
        screen = QApplication.primaryScreen()
        screen_center = screen.availableGeometry().center()
        # Replace la fenêtre autour du centre de l'écran
        qr.moveCenter(screen_center)
        self.move(qr.topLeft())
        
    def valider2AF(self):
        valeur_totp=self.ui.lE_totp.text()
        if valeur_totp == "":
            self.ui.l_erreur.setText("Veuillez remplir tous les champs.")
        else:
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
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT secret FROM utilisateur WHERE identifiant = %s", (self.identifiant,))
                result = cursor.fetchone()
                secret=result["secret"]
                print(f"Secret récupéré : {secret}") 
                totp=pyotp.TOTP(secret)
                if totp.verify(valeur_totp):
                    cursor.execute("SELECT role FROM utilisateur WHERE identifiant = %s",(self.identifiant,))
                    result=cursor.fetchall()
                    role = result[0]['role']
                    print(result)
                    if result and result[0]['role'] == "prof":
                        self.accueil = AppBancMotProf(self.identifiant,role)
                        self.accueil.show()
                        self.close()
                    else:
                        self.accueil = AppBancMot(self.identifiant,role)
                        self.accueil.show()
                        self.close()
                else:
                    self.ui.l_erreur.setText("Code Invalide ! ")
            except mysql.connector.Error as e:
                self.afficher_message(f"Problème de connexion à la base de données : {e}")
                
#programme principal
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    monApplication = Double_Auth()
    sys.exit(app.exec())