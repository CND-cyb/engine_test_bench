# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authentifierNopgNT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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

class Ui_Connexion(object):
    def setupUi(self, Connexion):
        if not Connexion.objectName():
            Connexion.setObjectName(u"Connexion")
        Connexion.resize(456, 300)
        Connexion.setStyleSheet(u"QWidget {\n"
"    background-color: #dfe6e9;\n"
"    color: #2d3436;\n"
"}")
        self.pb_connecter = QPushButton(Connexion)
        self.pb_connecter.setObjectName(u"pb_connecter")
        self.pb_connecter.setGeometry(QRect(160, 240, 121, 31))
        self.pb_connecter.setStyleSheet(u"QPushButton {\n"
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
        self.le_identifiant = QLineEdit(Connexion)
        self.le_identifiant.setObjectName(u"le_identifiant")
        self.le_identifiant.setGeometry(QRect(170, 80, 181, 31))
        self.le_identifiant.setStyleSheet(u"QLineEdit {\n"
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
        self.le_mdp = QLineEdit(Connexion)
        self.le_mdp.setObjectName(u"le_mdp")
        self.le_mdp.setGeometry(QRect(170, 130, 181, 31))
        self.le_mdp.setStyleSheet(u"QLineEdit {\n"
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
        self.label = QLabel(Connexion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 130, 71, 31))
        self.label_2 = QLabel(Connexion)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 80, 61, 31))
        self.l_erreur = QLabel(Connexion)
        self.l_erreur.setObjectName(u"l_erreur")
        self.l_erreur.setGeometry(QRect(90, 170, 241, 51))

        self.retranslateUi(Connexion)
        self.pb_connecter.clicked.connect(Connexion.authentifier)

        QMetaObject.connectSlotsByName(Connexion)
    # setupUi

    def retranslateUi(self, Connexion):
        Connexion.setWindowTitle(QCoreApplication.translate("Connexion", u"Form", None))
        self.pb_connecter.setText(QCoreApplication.translate("Connexion", u"Se connecter", None))
        self.label.setText(QCoreApplication.translate("Connexion", u"Mot de passe", None))
        self.label_2.setText(QCoreApplication.translate("Connexion", u"Identifiant", None))
        self.l_erreur.setText("")
    # retranslateUi
