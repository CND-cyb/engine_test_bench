from double_authentification_ui import Ui_Double_Auth
import sys
import mysql.connector
import bcrypt
from PyQt6.QtWidgets import QApplication, QWidget
from authentifier import Ui_Connexion
from CAccueil import AppBancMot  

class Double_Auth(QWidget):
    def __init__(self,identifiant):
        super().__init__()
        self.ui = Ui_Double_Auth()
        self.identifiant = identifiant
        self.ui.setupUi(self)
        self.show()
#programme principal
app = QApplication(sys.argv)
monApplication = Double_Auth()