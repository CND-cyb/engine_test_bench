# Form implementation generated from reading ui file 'double_authentification.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Double_Auth(object):
    def setupUi(self, Double_Auth):
        Double_Auth.setObjectName("Double_Auth")
        Double_Auth.resize(571, 295)
        Double_Auth.setStyleSheet("QWidget {\n"
"    background-color: #dfe6e9;\n"
"    color: #2d3436;\n"
"}")
        self.label = QtWidgets.QLabel(parent=Double_Auth)
        self.label.setGeometry(QtCore.QRect(150, 50, 131, 51))
        self.label.setObjectName("label")
        self.lE_totp = QtWidgets.QLineEdit(parent=Double_Auth)
        self.lE_totp.setGeometry(QtCore.QRect(260, 60, 141, 31))
        self.lE_totp.setStyleSheet("QLineEdit {\n"
"    background-color: #ecf0f1;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #2c3e50;\n"
"    font: 12px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3498db;\n"
"}")
        self.lE_totp.setObjectName("lE_totp")
        self.pb_envoyer_code2AF = QtWidgets.QPushButton(parent=Double_Auth)
        self.pb_envoyer_code2AF.setGeometry(QtCore.QRect(250, 160, 91, 31))
        self.pb_envoyer_code2AF.setStyleSheet("QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}")
        self.pb_envoyer_code2AF.setObjectName("pb_envoyer_code2AF")
        self.pb_2AF_retourAccueil = QtWidgets.QPushButton(parent=Double_Auth)
        self.pb_2AF_retourAccueil.setGeometry(QtCore.QRect(260, 230, 75, 31))
        self.pb_2AF_retourAccueil.setStyleSheet("QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}")
        self.pb_2AF_retourAccueil.setObjectName("pb_2AF_retourAccueil")
        self.l_erreur = QtWidgets.QLabel(parent=Double_Auth)
        self.l_erreur.setGeometry(QtCore.QRect(170, 100, 241, 41))
        self.l_erreur.setText("")
        self.l_erreur.setObjectName("l_erreur")

        self.retranslateUi(Double_Auth)
        QtCore.QMetaObject.connectSlotsByName(Double_Auth)

    def retranslateUi(self, Double_Auth):
        _translate = QtCore.QCoreApplication.translate
        Double_Auth.setWindowTitle(_translate("Double_Auth", "Double authentification - Banc d\'essais moteur"))
        self.label.setText(_translate("Double_Auth", "Code à usage \n"
" unique "))
        self.pb_envoyer_code2AF.setText(_translate("Double_Auth", "Envoyer"))
        self.pb_2AF_retourAccueil.setText(_translate("Double_Auth", "Retour"))
