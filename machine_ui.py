# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machineeaQEXX.ui'
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
        self.radioButton_5 = QRadioButton(Form)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(120, 140, 211, 20))
        self.radioButton_6 = QRadioButton(Form)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(120, 240, 251, 20))
        self.radioButton_7 = QRadioButton(Form)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(120, 190, 231, 20))
        self.radioButton_8 = QRadioButton(Form)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(410, 290, 241, 20))
        self.radioButton_9 = QRadioButton(Form)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setGeometry(QRect(410, 240, 271, 20))
        self.radioButton_10 = QRadioButton(Form)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setGeometry(QRect(410, 190, 261, 20))
        self.radioButton_11 = QRadioButton(Form)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setGeometry(QRect(120, 290, 261, 20))
        self.radioButton_12 = QRadioButton(Form)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(410, 140, 241, 20))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 360, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 430, 75, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"Moteur asynchrone 300 W (MAS)", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.18 kW (Mcc)", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"Moteur asynchrone 1.5 kW (MAS)", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 1.5 kW (Mcc)", None))
        self.radioButton_9.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 1.15 kW (Mcc)", None))
        self.radioButton_10.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.85 kW (Mcc)", None))
        self.radioButton_11.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.46 kW (Mcc)", None))
        self.radioButton_12.setText(QCoreApplication.translate("Form", u"Moteur \u00e0 courant continu 0.7 kW (Mcc)", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choix du type de moteur ", None))
    # retranslateUi

