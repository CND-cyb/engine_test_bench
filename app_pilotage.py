import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_pilotage_frein_manuel import Ui_Form

class AppPilotage(QWidget):
    def __init__(self):
        super().__init__()
        #Utilisation de Ui_Ui_utilisationQTableWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.sB_valeurFrein.valueChanged.connect(self.modifierSpinBox)
        self.ui.slider_valeurFrein.valueChanged.connect(self.modifierSlider)
        self.show()
    
    def modifierSpinBox(self):
        valeur = int(self.ui.sB_valeurFrein.value())
        print(valeur)
        self.ui.slider_valeurFrein.setValue(valeur)

    def modifierSlider(self):
        valeur = int(self.ui.slider_valeurFrein.value())
        self.ui.sB_valeurFrein.setValue(valeur)
        
#programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppPilotage()
    sys.exit(app.exec())
