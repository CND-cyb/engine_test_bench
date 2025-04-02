# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pilotage_frein_profil.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(961, 571)
        self.cB_choix_profil = QComboBox(Form)
        self.cB_choix_profil.addItem("")
        self.cB_choix_profil.addItem("")
        self.cB_choix_profil.addItem("")
        self.cB_choix_profil.addItem("")
        self.cB_choix_profil.addItem("")
        self.cB_choix_profil.setObjectName(u"cB_choix_profil")
        self.cB_choix_profil.setGeometry(QRect(310, 60, 331, 31))
        self.cB_choix_profil.setStyleSheet(u"QComboBox {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    padding: 6px 30px 6px 6px;\n"
"    font: 13px;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #b2bec3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    selection-background-color: #636e72;\n"
"    selection-color: #ffffff;\n"
"}")
        self.pb_choisir_frein_profil = QPushButton(Form)
        self.pb_choisir_frein_profil.setObjectName(u"pb_choisir_frein_profil")
        self.pb_choisir_frein_profil.setGeometry(QRect(420, 100, 81, 31))
        self.pb_choisir_frein_profil.setStyleSheet(u"QPushButton {\n"
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
        self.label.setGeometry(QRect(390, 20, 171, 31))
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 140, 861, 361))
        self.profil1 = QWidget()
        self.profil1.setObjectName(u"profil1")
        self.label_5 = QLabel(self.profil1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 50, 91, 31))
        self.pb_valider_profil1 = QPushButton(self.profil1)
        self.pb_valider_profil1.setObjectName(u"pb_valider_profil1")
        self.pb_valider_profil1.setGeometry(QRect(40, 110, 91, 31))
        self.pb_valider_profil1.setStyleSheet(u"QPushButton {\n"
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
        self.sB_coupleInitial = QSpinBox(self.profil1)
        self.sB_coupleInitial.setObjectName(u"sB_coupleInitial")
        self.sB_coupleInitial.setGeometry(QRect(130, 50, 61, 31))
        self.sB_coupleInitial.setMaximum(10000)
        self.sB_coupleInitial.setSingleStep(10)
        self.label_6 = QLabel(self.profil1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(620, 10, 171, 21))
        self.label_7 = QLabel(self.profil1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(380, 20, 51, 16))
        self.l_profil1_tension = QLabel(self.profil1)
        self.l_profil1_tension.setObjectName(u"l_profil1_tension")
        self.l_profil1_tension.setGeometry(QRect(330, 50, 51, 21))
        self.l_profil1_courant = QLabel(self.profil1)
        self.l_profil1_courant.setObjectName(u"l_profil1_courant")
        self.l_profil1_courant.setGeometry(QRect(325, 90, 52, 16))
        self.l_profil1_vitesse = QLabel(self.profil1)
        self.l_profil1_vitesse.setObjectName(u"l_profil1_vitesse")
        self.l_profil1_vitesse.setGeometry(QRect(335, 120, 41, 21))
        self.l_profil1_pUtile = QLabel(self.profil1)
        self.l_profil1_pUtile.setObjectName(u"l_profil1_pUtile")
        self.l_profil1_pUtile.setGeometry(QRect(340, 190, 41, 31))
        self.l_profil1_couple = QLabel(self.profil1)
        self.l_profil1_couple.setObjectName(u"l_profil1_couple")
        self.l_profil1_couple.setGeometry(QRect(333, 150, 51, 31))
        self.l_profil1_moteur_couple = QLabel(self.profil1)
        self.l_profil1_moteur_couple.setObjectName(u"l_profil1_moteur_couple")
        self.l_profil1_moteur_couple.setGeometry(QRect(612, 120, 51, 21))
        self.l_profil1_moteur_pUtile = QLabel(self.profil1)
        self.l_profil1_moteur_pUtile.setObjectName(u"l_profil1_moteur_pUtile")
        self.l_profil1_moteur_pUtile.setGeometry(QRect(618, 150, 51, 31))
        self.l_profil1_moteur_courant = QLabel(self.profil1)
        self.l_profil1_moteur_courant.setObjectName(u"l_profil1_moteur_courant")
        self.l_profil1_moteur_courant.setGeometry(QRect(605, 90, 52, 16))
        self.l_profil1_moteur_tension = QLabel(self.profil1)
        self.l_profil1_moteur_tension.setObjectName(u"l_profil1_moteur_tension")
        self.l_profil1_moteur_tension.setGeometry(QRect(610, 50, 51, 21))
        self.l_profil1_typeMoteur = QLabel(self.profil1)
        self.l_profil1_typeMoteur.setObjectName(u"l_profil1_typeMoteur")
        self.l_profil1_typeMoteur.setGeometry(QRect(610, 190, 131, 16))
        self.label_34 = QLabel(self.profil1)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(198, 50, 51, 31))
        self.pb_retour_profil1 = QPushButton(self.profil1)
        self.pb_retour_profil1.setObjectName(u"pb_retour_profil1")
        self.pb_retour_profil1.setGeometry(QRect(349, 273, 101, 31))
        self.pb_retour_profil1.setStyleSheet(u"QPushButton {\n"
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
        self.tabWidget.addTab(self.profil1, "")
        self.profil2 = QWidget()
        self.profil2.setObjectName(u"profil2")
        self.l_profil1_vitesse_2 = QLabel(self.profil2)
        self.l_profil1_vitesse_2.setObjectName(u"l_profil1_vitesse_2")
        self.l_profil1_vitesse_2.setGeometry(QRect(335, 120, 41, 21))
        self.l_profil1_couple_2 = QLabel(self.profil2)
        self.l_profil1_couple_2.setObjectName(u"l_profil1_couple_2")
        self.l_profil1_couple_2.setGeometry(QRect(333, 150, 51, 31))
        self.l_profil1_courant_2 = QLabel(self.profil2)
        self.l_profil1_courant_2.setObjectName(u"l_profil1_courant_2")
        self.l_profil1_courant_2.setGeometry(QRect(325, 90, 52, 16))
        self.l_profil1_moteur_tension_2 = QLabel(self.profil2)
        self.l_profil1_moteur_tension_2.setObjectName(u"l_profil1_moteur_tension_2")
        self.l_profil1_moteur_tension_2.setGeometry(QRect(610, 50, 51, 21))
        self.l_profil1_moteur_couple_2 = QLabel(self.profil2)
        self.l_profil1_moteur_couple_2.setObjectName(u"l_profil1_moteur_couple_2")
        self.l_profil1_moteur_couple_2.setGeometry(QRect(612, 120, 51, 21))
        self.l_profil1_moteur_pUtile_2 = QLabel(self.profil2)
        self.l_profil1_moteur_pUtile_2.setObjectName(u"l_profil1_moteur_pUtile_2")
        self.l_profil1_moteur_pUtile_2.setGeometry(QRect(618, 150, 51, 31))
        self.label_8 = QLabel(self.profil2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(380, 20, 51, 16))
        self.l_profil1_pUtile_2 = QLabel(self.profil2)
        self.l_profil1_pUtile_2.setObjectName(u"l_profil1_pUtile_2")
        self.l_profil1_pUtile_2.setGeometry(QRect(340, 190, 41, 31))
        self.label_9 = QLabel(self.profil2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(620, 10, 171, 21))
        self.l_profil1_tension_2 = QLabel(self.profil2)
        self.l_profil1_tension_2.setObjectName(u"l_profil1_tension_2")
        self.l_profil1_tension_2.setGeometry(QRect(330, 50, 51, 21))
        self.l_profil1_typeMoteur_2 = QLabel(self.profil2)
        self.l_profil1_typeMoteur_2.setObjectName(u"l_profil1_typeMoteur_2")
        self.l_profil1_typeMoteur_2.setGeometry(QRect(610, 190, 131, 16))
        self.l_profil1_moteur_courant_2 = QLabel(self.profil2)
        self.l_profil1_moteur_courant_2.setObjectName(u"l_profil1_moteur_courant_2")
        self.l_profil1_moteur_courant_2.setGeometry(QRect(605, 90, 52, 16))
        self.label_16 = QLabel(self.profil2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 50, 121, 31))
        self.sB_coefficientDirecteur_profil2 = QSpinBox(self.profil2)
        self.sB_coefficientDirecteur_profil2.setObjectName(u"sB_coefficientDirecteur_profil2")
        self.sB_coefficientDirecteur_profil2.setGeometry(QRect(140, 50, 61, 31))
        self.sB_coefficientDirecteur_profil2.setMaximum(10000)
        self.sB_coefficientDirecteur_profil2.setSingleStep(10)
        self.label_17 = QLabel(self.profil2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 110, 121, 31))
        self.sB_ordonneeOrigine_profil2 = QSpinBox(self.profil2)
        self.sB_ordonneeOrigine_profil2.setObjectName(u"sB_ordonneeOrigine_profil2")
        self.sB_ordonneeOrigine_profil2.setGeometry(QRect(140, 110, 61, 31))
        self.sB_ordonneeOrigine_profil2.setMaximum(10000)
        self.sB_ordonneeOrigine_profil2.setSingleStep(10)
        self.pb_valider_profil2 = QPushButton(self.profil2)
        self.pb_valider_profil2.setObjectName(u"pb_valider_profil2")
        self.pb_valider_profil2.setGeometry(QRect(60, 170, 101, 31))
        self.pb_retour_profil2 = QPushButton(self.profil2)
        self.pb_retour_profil2.setObjectName(u"pb_retour_profil2")
        self.pb_retour_profil2.setGeometry(QRect(349, 273, 101, 31))
        self.pb_retour_profil2.setStyleSheet(u"QPushButton {\n"
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
        self.tabWidget.addTab(self.profil2, "")
        self.profil3 = QWidget()
        self.profil3.setObjectName(u"profil3")
        self.l_profil1_vitesse_3 = QLabel(self.profil3)
        self.l_profil1_vitesse_3.setObjectName(u"l_profil1_vitesse_3")
        self.l_profil1_vitesse_3.setGeometry(QRect(335, 120, 41, 21))
        self.l_profil1_couple_3 = QLabel(self.profil3)
        self.l_profil1_couple_3.setObjectName(u"l_profil1_couple_3")
        self.l_profil1_couple_3.setGeometry(QRect(333, 150, 51, 31))
        self.l_profil1_courant_3 = QLabel(self.profil3)
        self.l_profil1_courant_3.setObjectName(u"l_profil1_courant_3")
        self.l_profil1_courant_3.setGeometry(QRect(325, 90, 52, 16))
        self.l_profil1_moteur_tension_3 = QLabel(self.profil3)
        self.l_profil1_moteur_tension_3.setObjectName(u"l_profil1_moteur_tension_3")
        self.l_profil1_moteur_tension_3.setGeometry(QRect(610, 50, 51, 21))
        self.l_profil1_moteur_couple_3 = QLabel(self.profil3)
        self.l_profil1_moteur_couple_3.setObjectName(u"l_profil1_moteur_couple_3")
        self.l_profil1_moteur_couple_3.setGeometry(QRect(612, 120, 51, 21))
        self.l_profil1_moteur_pUtile_3 = QLabel(self.profil3)
        self.l_profil1_moteur_pUtile_3.setObjectName(u"l_profil1_moteur_pUtile_3")
        self.l_profil1_moteur_pUtile_3.setGeometry(QRect(618, 150, 51, 31))
        self.label_10 = QLabel(self.profil3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(380, 20, 51, 16))
        self.l_profil1_pUtile_3 = QLabel(self.profil3)
        self.l_profil1_pUtile_3.setObjectName(u"l_profil1_pUtile_3")
        self.l_profil1_pUtile_3.setGeometry(QRect(340, 190, 41, 31))
        self.label_11 = QLabel(self.profil3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(620, 10, 171, 21))
        self.l_profil1_tension_3 = QLabel(self.profil3)
        self.l_profil1_tension_3.setObjectName(u"l_profil1_tension_3")
        self.l_profil1_tension_3.setGeometry(QRect(330, 50, 51, 21))
        self.l_profil1_typeMoteur_3 = QLabel(self.profil3)
        self.l_profil1_typeMoteur_3.setObjectName(u"l_profil1_typeMoteur_3")
        self.l_profil1_typeMoteur_3.setGeometry(QRect(610, 190, 131, 16))
        self.l_profil1_moteur_courant_3 = QLabel(self.profil3)
        self.l_profil1_moteur_courant_3.setObjectName(u"l_profil1_moteur_courant_3")
        self.l_profil1_moteur_courant_3.setGeometry(QRect(605, 90, 52, 16))
        self.pb_retour_profil3 = QPushButton(self.profil3)
        self.pb_retour_profil3.setObjectName(u"pb_retour_profil3")
        self.pb_retour_profil3.setGeometry(QRect(349, 273, 101, 31))
        self.pb_retour_profil3.setStyleSheet(u"QPushButton {\n"
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
        self.pb_valider_profil3 = QPushButton(self.profil3)
        self.pb_valider_profil3.setObjectName(u"pb_valider_profil3")
        self.pb_valider_profil3.setGeometry(QRect(60, 170, 91, 31))
        self.pb_valider_profil3.setStyleSheet(u"QPushButton {\n"
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
        self.label_19 = QLabel(self.profil3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 110, 111, 31))
        self.label_18 = QLabel(self.profil3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 50, 111, 31))
        self.sB_ordonneeOrigine_profil3 = QSpinBox(self.profil3)
        self.sB_ordonneeOrigine_profil3.setObjectName(u"sB_ordonneeOrigine_profil3")
        self.sB_ordonneeOrigine_profil3.setGeometry(QRect(140, 110, 61, 31))
        self.sB_ordonneeOrigine_profil3.setMaximum(10000)
        self.sB_ordonneeOrigine_profil3.setSingleStep(10)
        self.sB_coefficientDirecteur_profil3 = QSpinBox(self.profil3)
        self.sB_coefficientDirecteur_profil3.setObjectName(u"sB_coefficientDirecteur_profil3")
        self.sB_coefficientDirecteur_profil3.setGeometry(QRect(140, 50, 61, 31))
        self.sB_coefficientDirecteur_profil3.setMaximum(10000)
        self.sB_coefficientDirecteur_profil3.setSingleStep(10)
        self.tabWidget.addTab(self.profil3, "")
        self.profil4 = QWidget()
        self.profil4.setObjectName(u"profil4")
        self.sB_coefficientDirecteur_profil4 = QSpinBox(self.profil4)
        self.sB_coefficientDirecteur_profil4.setObjectName(u"sB_coefficientDirecteur_profil4")
        self.sB_coefficientDirecteur_profil4.setGeometry(QRect(150, 140, 61, 31))
        self.sB_coefficientDirecteur_profil4.setMaximum(10000)
        self.sB_coefficientDirecteur_profil4.setSingleStep(10)
        self.sB_dureeConstante_profil4 = QSpinBox(self.profil4)
        self.sB_dureeConstante_profil4.setObjectName(u"sB_dureeConstante_profil4")
        self.sB_dureeConstante_profil4.setGeometry(QRect(150, 90, 61, 31))
        self.sB_dureeConstante_profil4.setMaximum(10000)
        self.sB_dureeConstante_profil4.setSingleStep(10)
        self.sB_coupleInitial_profil4 = QSpinBox(self.profil4)
        self.sB_coupleInitial_profil4.setObjectName(u"sB_coupleInitial_profil4")
        self.sB_coupleInitial_profil4.setGeometry(QRect(150, 40, 61, 31))
        self.sB_coupleInitial_profil4.setMaximum(10000)
        self.sB_coupleInitial_profil4.setSingleStep(10)
        self.label_2 = QLabel(self.profil4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 40, 91, 31))
        self.label_3 = QLabel(self.profil4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 89, 101, 31))
        self.label_4 = QLabel(self.profil4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 140, 141, 31))
        self.pb_valider_profil4 = QPushButton(self.profil4)
        self.pb_valider_profil4.setObjectName(u"pb_valider_profil4")
        self.pb_valider_profil4.setGeometry(QRect(64, 193, 91, 31))
        self.pb_valider_profil4.setStyleSheet(u"QPushButton {\n"
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
        self.l_profil4_vitesse = QLabel(self.profil4)
        self.l_profil4_vitesse.setObjectName(u"l_profil4_vitesse")
        self.l_profil4_vitesse.setGeometry(QRect(335, 120, 41, 21))
        self.l_profil4_couple = QLabel(self.profil4)
        self.l_profil4_couple.setObjectName(u"l_profil4_couple")
        self.l_profil4_couple.setGeometry(QRect(333, 150, 51, 31))
        self.l_profil4_courant = QLabel(self.profil4)
        self.l_profil4_courant.setObjectName(u"l_profil4_courant")
        self.l_profil4_courant.setGeometry(QRect(325, 90, 52, 16))
        self.l_profil4_moteur_tension = QLabel(self.profil4)
        self.l_profil4_moteur_tension.setObjectName(u"l_profil4_moteur_tension")
        self.l_profil4_moteur_tension.setGeometry(QRect(610, 50, 51, 21))
        self.l_profil4_moteur_couple = QLabel(self.profil4)
        self.l_profil4_moteur_couple.setObjectName(u"l_profil4_moteur_couple")
        self.l_profil4_moteur_couple.setGeometry(QRect(612, 120, 51, 21))
        self.l_profil4_moteur_pUtile = QLabel(self.profil4)
        self.l_profil4_moteur_pUtile.setObjectName(u"l_profil4_moteur_pUtile")
        self.l_profil4_moteur_pUtile.setGeometry(QRect(618, 150, 51, 31))
        self.label_12 = QLabel(self.profil4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(380, 20, 51, 16))
        self.l_profil4_pUtile = QLabel(self.profil4)
        self.l_profil4_pUtile.setObjectName(u"l_profil4_pUtile")
        self.l_profil4_pUtile.setGeometry(QRect(340, 190, 41, 31))
        self.label_13 = QLabel(self.profil4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(620, 10, 171, 21))
        self.l_profil4_tension = QLabel(self.profil4)
        self.l_profil4_tension.setObjectName(u"l_profil4_tension")
        self.l_profil4_tension.setGeometry(QRect(330, 50, 51, 21))
        self.l_profil4_typeMoteur = QLabel(self.profil4)
        self.l_profil4_typeMoteur.setObjectName(u"l_profil4_typeMoteur")
        self.l_profil4_typeMoteur.setGeometry(QRect(610, 190, 131, 16))
        self.l_profil4_moteur_courant = QLabel(self.profil4)
        self.l_profil4_moteur_courant.setObjectName(u"l_profil4_moteur_courant")
        self.l_profil4_moteur_courant.setGeometry(QRect(605, 90, 52, 16))
        self.pb_retour_profil4 = QPushButton(self.profil4)
        self.pb_retour_profil4.setObjectName(u"pb_retour_profil4")
        self.pb_retour_profil4.setGeometry(QRect(349, 273, 101, 31))
        self.pb_retour_profil4.setStyleSheet(u"QPushButton {\n"
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
        self.tabWidget.addTab(self.profil4, "")
        self.profil5 = QWidget()
        self.profil5.setObjectName(u"profil5")
        self.l_profil1_vitesse_5 = QLabel(self.profil5)
        self.l_profil1_vitesse_5.setObjectName(u"l_profil1_vitesse_5")
        self.l_profil1_vitesse_5.setGeometry(QRect(335, 120, 41, 21))
        self.l_profil1_couple_5 = QLabel(self.profil5)
        self.l_profil1_couple_5.setObjectName(u"l_profil1_couple_5")
        self.l_profil1_couple_5.setGeometry(QRect(333, 150, 51, 31))
        self.l_profil1_courant_5 = QLabel(self.profil5)
        self.l_profil1_courant_5.setObjectName(u"l_profil1_courant_5")
        self.l_profil1_courant_5.setGeometry(QRect(325, 90, 52, 16))
        self.l_profil1_moteur_tension_5 = QLabel(self.profil5)
        self.l_profil1_moteur_tension_5.setObjectName(u"l_profil1_moteur_tension_5")
        self.l_profil1_moteur_tension_5.setGeometry(QRect(610, 50, 51, 21))
        self.l_profil1_moteur_couple_5 = QLabel(self.profil5)
        self.l_profil1_moteur_couple_5.setObjectName(u"l_profil1_moteur_couple_5")
        self.l_profil1_moteur_couple_5.setGeometry(QRect(612, 120, 51, 21))
        self.l_profil1_moteur_pUtile_5 = QLabel(self.profil5)
        self.l_profil1_moteur_pUtile_5.setObjectName(u"l_profil1_moteur_pUtile_5")
        self.l_profil1_moteur_pUtile_5.setGeometry(QRect(618, 150, 51, 31))
        self.label_14 = QLabel(self.profil5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(380, 20, 51, 16))
        self.l_profil1_pUtile_5 = QLabel(self.profil5)
        self.l_profil1_pUtile_5.setObjectName(u"l_profil1_pUtile_5")
        self.l_profil1_pUtile_5.setGeometry(QRect(340, 190, 41, 31))
        self.label_15 = QLabel(self.profil5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(620, 10, 171, 21))
        self.l_profil1_tension_5 = QLabel(self.profil5)
        self.l_profil1_tension_5.setObjectName(u"l_profil1_tension_5")
        self.l_profil1_tension_5.setGeometry(QRect(330, 50, 51, 21))
        self.l_profil1_typeMoteur_5 = QLabel(self.profil5)
        self.l_profil1_typeMoteur_5.setObjectName(u"l_profil1_typeMoteur_5")
        self.l_profil1_typeMoteur_5.setGeometry(QRect(610, 190, 131, 16))
        self.l_profil1_moteur_courant_5 = QLabel(self.profil5)
        self.l_profil1_moteur_courant_5.setObjectName(u"l_profil1_moteur_courant_5")
        self.l_profil1_moteur_courant_5.setGeometry(QRect(605, 90, 52, 16))
        self.label_35 = QLabel(self.profil5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(50, 40, 121, 31))
        self.sB_coupleEtatHaut_profil5 = QSpinBox(self.profil5)
        self.sB_coupleEtatHaut_profil5.setObjectName(u"sB_coupleEtatHaut_profil5")
        self.sB_coupleEtatHaut_profil5.setGeometry(QRect(150, 40, 61, 31))
        self.sB_coupleEtatHaut_profil5.setMaximum(10000)
        self.sB_coupleEtatHaut_profil5.setSingleStep(10)
        self.label_36 = QLabel(self.profil5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(50, 90, 121, 31))
        self.sB_coupleEtatBas_profil5 = QSpinBox(self.profil5)
        self.sB_coupleEtatBas_profil5.setObjectName(u"sB_coupleEtatBas_profil5")
        self.sB_coupleEtatBas_profil5.setGeometry(QRect(150, 90, 61, 31))
        self.sB_coupleEtatBas_profil5.setMaximum(10000)
        self.sB_coupleEtatBas_profil5.setSingleStep(10)
        self.label_37 = QLabel(self.profil5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(50, 140, 121, 31))
        self.sB_dureeEtatHaut_profil5 = QSpinBox(self.profil5)
        self.sB_dureeEtatHaut_profil5.setObjectName(u"sB_dureeEtatHaut_profil5")
        self.sB_dureeEtatHaut_profil5.setGeometry(QRect(150, 140, 61, 31))
        self.sB_dureeEtatHaut_profil5.setMaximum(10000)
        self.sB_dureeEtatHaut_profil5.setSingleStep(10)
        self.label_38 = QLabel(self.profil5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(50, 190, 121, 31))
        self.sB_dureeEtatBas_profil5 = QSpinBox(self.profil5)
        self.sB_dureeEtatBas_profil5.setObjectName(u"sB_dureeEtatBas_profil5")
        self.sB_dureeEtatBas_profil5.setGeometry(QRect(150, 190, 61, 31))
        self.sB_dureeEtatBas_profil5.setMaximum(10000)
        self.sB_dureeEtatBas_profil5.setSingleStep(10)
        self.label_39 = QLabel(self.profil5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(220, 40, 51, 31))
        self.label_40 = QLabel(self.profil5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(220, 90, 51, 31))
        self.label_41 = QLabel(self.profil5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(220, 140, 51, 31))
        self.label_42 = QLabel(self.profil5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(220, 190, 51, 31))
        self.pb_retour_profil5 = QPushButton(self.profil5)
        self.pb_retour_profil5.setObjectName(u"pb_retour_profil5")
        self.pb_retour_profil5.setGeometry(QRect(349, 273, 101, 31))
        self.pb_retour_profil5.setStyleSheet(u"QPushButton {\n"
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
        self.pb_valider_profil5 = QPushButton(self.profil5)
        self.pb_valider_profil5.setObjectName(u"pb_valider_profil5")
        self.pb_valider_profil5.setGeometry(QRect(90, 240, 91, 31))
        self.pb_valider_profil5.setStyleSheet(u"QPushButton {\n"
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
        self.tabWidget.addTab(self.profil5, "")
        self.pb_frein_profil_quitter = QPushButton(Form)
        self.pb_frein_profil_quitter.setObjectName(u"pb_frein_profil_quitter")
        self.pb_frein_profil_quitter.setGeometry(QRect(400, 521, 101, 31))
        self.pb_frein_profil_quitter.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cB_choix_profil.setItemText(0, QCoreApplication.translate("Form", u"Couple constant : T = B", None))
        self.cB_choix_profil.setItemText(1, QCoreApplication.translate("Form", u"Couple de type : T = An+B", None))
        self.cB_choix_profil.setItemText(2, QCoreApplication.translate("Form", u"Couple de type : T = An\u00b2+B", None))
        self.cB_choix_profil.setItemText(3, QCoreApplication.translate("Form", u"Couple de type : T = An\u22121", None))
        self.cB_choix_profil.setItemText(4, QCoreApplication.translate("Form", u"Couple de commande impulsionnelle", None))

        self.pb_choisir_frein_profil.setText(QCoreApplication.translate("Form", u"Choisir", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choisissez le profil voulu", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Couple Initial : ", None))
        self.pb_valider_profil1.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Caract\u00e9ristiques du moteur ", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Valeurs", None))
        self.l_profil1_tension.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_courant.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.l_profil1_vitesse.setText(QCoreApplication.translate("Form", u"Vitesse :", None))
        self.l_profil1_pUtile.setText(QCoreApplication.translate("Form", u"PUtile : ", None))
        self.l_profil1_couple.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_moteur_couple.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_moteur_pUtile.setText(QCoreApplication.translate("Form", u"PUtile :", None))
        self.l_profil1_moteur_courant.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.l_profil1_moteur_tension.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_typeMoteur.setText(QCoreApplication.translate("Form", u"Type de Moteur : ", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Nm", None))
        self.pb_retour_profil1.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profil1), QCoreApplication.translate("Form", u"Profil 1", None))
        self.l_profil1_vitesse_2.setText(QCoreApplication.translate("Form", u"Vitesse :", None))
        self.l_profil1_couple_2.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_courant_2.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.l_profil1_moteur_tension_2.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_moteur_couple_2.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_moteur_pUtile_2.setText(QCoreApplication.translate("Form", u"PUtile :", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Valeurs", None))
        self.l_profil1_pUtile_2.setText(QCoreApplication.translate("Form", u"PUtile : ", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Caract\u00e9ristiques du moteur ", None))
        self.l_profil1_tension_2.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_typeMoteur_2.setText(QCoreApplication.translate("Form", u"Type de Moteur : ", None))
        self.l_profil1_moteur_courant_2.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Coefficient directeur \n"
"de la courbe ", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Ordonn\u00e9e \u00e0 l'origine \n"
"de la courbe ", None))
        self.pb_valider_profil2.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.pb_retour_profil2.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profil2), QCoreApplication.translate("Form", u"Profil 2", None))
        self.l_profil1_vitesse_3.setText(QCoreApplication.translate("Form", u"Vitesse :", None))
        self.l_profil1_couple_3.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_courant_3.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.l_profil1_moteur_tension_3.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_moteur_couple_3.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_moteur_pUtile_3.setText(QCoreApplication.translate("Form", u"PUtile :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Valeurs", None))
        self.l_profil1_pUtile_3.setText(QCoreApplication.translate("Form", u"PUtile : ", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Caract\u00e9ristiques du moteur ", None))
        self.l_profil1_tension_3.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_typeMoteur_3.setText(QCoreApplication.translate("Form", u"Type de Moteur : ", None))
        self.l_profil1_moteur_courant_3.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.pb_retour_profil3.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.pb_valider_profil3.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Ordonn\u00e9e \u00e0 l'origine \n"
"de la courbe", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Coefficient directeur  \n"
"de la courbe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profil3), QCoreApplication.translate("Form", u"Profil 3", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Couple Initial : ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Dur\u00e9e constante : ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Coefficient directeur\n"
" de la pente : ", None))
        self.pb_valider_profil4.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.l_profil4_vitesse.setText(QCoreApplication.translate("Form", u"Vitesse :", None))
        self.l_profil4_couple.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil4_courant.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.l_profil4_moteur_tension.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil4_moteur_couple.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil4_moteur_pUtile.setText(QCoreApplication.translate("Form", u"PUtile :", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Valeurs", None))
        self.l_profil4_pUtile.setText(QCoreApplication.translate("Form", u"PUtile : ", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Caract\u00e9ristiques du moteur ", None))
        self.l_profil4_tension.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil4_typeMoteur.setText(QCoreApplication.translate("Form", u"Type de Moteur : ", None))
        self.l_profil4_moteur_courant.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.pb_retour_profil4.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profil4), QCoreApplication.translate("Form", u"Profil 4 ", None))
        self.l_profil1_vitesse_5.setText(QCoreApplication.translate("Form", u"Vitesse :", None))
        self.l_profil1_couple_5.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_courant_5.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.l_profil1_moteur_tension_5.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_moteur_couple_5.setText(QCoreApplication.translate("Form", u"Couple :", None))
        self.l_profil1_moteur_pUtile_5.setText(QCoreApplication.translate("Form", u"PUtile :", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Valeurs", None))
        self.l_profil1_pUtile_5.setText(QCoreApplication.translate("Form", u"PUtile : ", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Caract\u00e9ristiques du moteur ", None))
        self.l_profil1_tension_5.setText(QCoreApplication.translate("Form", u"Tension :", None))
        self.l_profil1_typeMoteur_5.setText(QCoreApplication.translate("Form", u"Type de Moteur : ", None))
        self.l_profil1_moteur_courant_5.setText(QCoreApplication.translate("Form", u"Courant  :", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Couple Etat Haut", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Couple Etat Bas", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Dur\u00e9e Etat Haut ", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Dur\u00e9e Etat Bas ", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Nm", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"Nm", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"secondes", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"secondes", None))
        self.pb_retour_profil5.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.pb_valider_profil5.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profil5), QCoreApplication.translate("Form", u"Profil 5", None))
        self.pb_frein_profil_quitter.setText(QCoreApplication.translate("Form", u"Quitter", None))
    # retranslateUi

