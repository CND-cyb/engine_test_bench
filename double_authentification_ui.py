# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'double_authentification.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Double_Auth(object):
    def setupUi(self, Double_Auth):
        if not Double_Auth.objectName():
            Double_Auth.setObjectName(u"Double_Auth")
        Double_Auth.resize(371, 295)
        Double_Auth.setStyleSheet(u"QWidget {\n"
"    background-color: #dfe6e9;\n"
"    color: #2d3436;\n"
"}")
        self.label = QLabel(Double_Auth)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 131, 51))
        self.lE_totp = QLineEdit(Double_Auth)
        self.lE_totp.setObjectName(u"lE_totp")
        self.lE_totp.setGeometry(QRect(150, 60, 141, 31))
        self.lE_totp.setStyleSheet(u"QLineEdit {\n"
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
        self.pb_envoyer_code2AF = QPushButton(Double_Auth)
        self.pb_envoyer_code2AF.setObjectName(u"pb_envoyer_code2AF")
        self.pb_envoyer_code2AF.setGeometry(QRect(140, 160, 91, 31))
        self.pb_envoyer_code2AF.setStyleSheet(u"QPushButton {\n"
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
        self.pb_2AF_retourAccueil = QPushButton(Double_Auth)
        self.pb_2AF_retourAccueil.setObjectName(u"pb_2AF_retourAccueil")
        self.pb_2AF_retourAccueil.setGeometry(QRect(150, 230, 75, 31))
        self.pb_2AF_retourAccueil.setStyleSheet(u"QPushButton {\n"
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
        self.l_erreur = QLabel(Double_Auth)
        self.l_erreur.setObjectName(u"l_erreur")
        self.l_erreur.setGeometry(QRect(60, 100, 241, 41))

        self.retranslateUi(Double_Auth)

        QMetaObject.connectSlotsByName(Double_Auth)
    # setupUi

    def retranslateUi(self, Double_Auth):
        Double_Auth.setWindowTitle(QCoreApplication.translate("Double_Auth", u"Double_Auth", None))
        self.label.setText(QCoreApplication.translate("Double_Auth", u"Code \u00e0 usage \n"
" unique ", None))
        self.pb_envoyer_code2AF.setText(QCoreApplication.translate("Double_Auth", u"Envoyer", None))
        self.pb_2AF_retourAccueil.setText(QCoreApplication.translate("Double_Auth", u"Retour", None))
        self.l_erreur.setText("")
    # retranslateUi

