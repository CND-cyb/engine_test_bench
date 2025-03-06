import sys
from PySide6.QtWidgets import QApplication, QWidget
from machine_ui import Ui_Form

class AppChoixMoteur(QWidget):
    def __init__(self):
        super().__init__()
        #Utilisation de Ui_Ui_utilisationQTableWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        
#programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppChoixMoteur()
    sys.exit(app.exec())
