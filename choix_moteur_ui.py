# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choix_moteurhKedEL.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(805, 523)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #dfe6e9;\n"
"    color: #2d3436;\n"
"}")
        self.rB_moteur1 = QRadioButton(Form)
        self.rB_moteur1.setObjectName(u"rB_moteur1")
        self.rB_moteur1.setGeometry(QRect(120, 140, 211, 20))
        self.rB_moteur3 = QRadioButton(Form)
        self.rB_moteur3.setObjectName(u"rB_moteur3")
        self.rB_moteur3.setGeometry(QRect(120, 240, 251, 20))
        self.rB_moteur2 = QRadioButton(Form)
        self.rB_moteur2.setObjectName(u"rB_moteur2")
        self.rB_moteur2.setGeometry(QRect(120, 190, 231, 20))
        self.rB_moteur8 = QRadioButton(Form)
        self.rB_moteur8.setObjectName(u"rB_moteur8")
        self.rB_moteur8.setGeometry(QRect(410, 290, 241, 20))
        self.rB_moteur7 = QRadioButton(Form)
        self.rB_moteur7.setObjectName(u"rB_moteur7")
        self.rB_moteur7.setGeometry(QRect(410, 240, 271, 20))
        self.rB_moteur6 = QRadioButton(Form)
        self.rB_moteur6.setObjectName(u"rB_moteur6")
        self.rB_moteur6.setGeometry(QRect(410, 190, 261, 20))
        self.rB_moteur4 = QRadioButton(Form)
        self.rB_moteur4.setObjectName(u"rB_moteur4")
        self.rB_moteur4.setGeometry(QRect(120, 290, 261, 20))
        self.rB_moteur5 = QRadioButton(Form)
        self.rB_moteur5.setObjectName(u"rB_moteur5")
        self.rB_moteur5.setGeometry(QRect(410, 140, 241, 20))
        self.pb_valider_machine = QPushButton(Form)
        self.pb_valider_machine.setObjectName(u"pb_valider_machine")
        self.pb_valider_machine.setGeometry(QRect(350, 360, 75, 31))
        self.pb_valider_machine.setStyleSheet(u"QPushButton {\n"
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
        self.pb_machineRetour_accueil = QPushButton(Form)
        self.pb_machineRetour_accueil.setObjectName(u"pb_machineRetour_accueil")
        self.pb_machineRetour_accueil.setGeometry(QRect(350, 430, 75, 31))
        self.pb_machineRetour_accueil.setStyleSheet(u"QPushButton {\n"
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 40, 201, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.rB_moteur1.setText(QCoreApplication.translate("Form", u"Moteur asynchrone 300 W (MAS)", None))
        self.rB_moteur3.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.18 kW (Mcc)", None))
        self.rB_moteur2.setText(QCoreApplication.translate("Form", u"Moteur asynchrone 1.5 kW (MAS)", None))
        self.rB_moteur8.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 1.5 kW (Mcc)", None))
        self.rB_moteur7.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 1.15 kW (Mcc)", None))
        self.rB_moteur6.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.85 kW (Mcc)", None))
        self.rB_moteur4.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.46 kW (Mcc)", None))
        self.rB_moteur5.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.7 kW (Mcc)", None))
        self.pb_valider_machine.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.pb_machineRetour_accueil.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choix du type de moteur ", None))
    # retranslateUi


