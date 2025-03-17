import sys
from PySide6.QtWidgets import QApplication, QWidget
from pilotage_frein_profil_ui import Ui_Form

class AppPilotage(QWidget):
    def __init__(self):
        super().__init__()
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
        self.ui.tabWidget.setCurrentIndex(0)
        self.show()

    def choisirProfil(self):
        index = self.ui.cB_choix_profil.currentIndex()
        if 0 <= index < self.ui.tabWidget.count():
            for i in range(self.ui.tabWidget.count()):
                self.ui.tabWidget.setTabEnabled(i, False)
            self.ui.tabWidget.setTabEnabled(index, True)
            self.ui.tabWidget.setCurrentIndex(index)
            
    def retourChoixProfil(self):
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabEnabled(i, False)
        
    def quitter(self):
        self.close()
        
# Programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppPilotage()
    sys.exit(app.exec())
