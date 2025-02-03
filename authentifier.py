import sys
from PyQt6.QtWidgets import QApplication, QWidget
from authentifier_ui import Ui_Connexion
import mysql.connector

# Informations de connexion
host = 'mysql-eguidat.alwaysdata.net'
user = 'eguidat_banc_mot'
password = 'CestGénialCeBts2025*!'
database = 'eguidat_banc_moteur'

class Login(QWidget):
    def __init__(self):
        super().__init__()

        # use the Ui_login_form
        self.ui = Ui_Connexion()       
        self.ui.setupUi(self)       
        
        self.ui.pb_connecter.clicked.connect(self.authentifier)
        # show the login window
        self.show()

    def authentifier():
        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())