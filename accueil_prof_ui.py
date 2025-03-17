# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accueil_prof.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QWidget)

class Ui_AppBancMot_prof(object):
    def setupUi(self, AppBancMot_prof):
        if not AppBancMot_prof.objectName():
            AppBancMot_prof.setObjectName(u"AppBancMot_prof")
        AppBancMot_prof.resize(1128, 609)
        self.tab_administration = QTabWidget(AppBancMot_prof)
        self.tab_administration.setObjectName(u"tab_administration")
        self.tab_administration.setGeometry(QRect(0, 0, 1141, 671))
        self.tab_administration.setStyleSheet(u"QTabWidget {\n"
"    background-color: #f9f9f9;  /* Couleur de fond du QTabWidget (gris clair) */\n"
"    border: 1px solid #d1d1d1;  /* Bordure du QTabWidget */\n"
"    border-radius: 5px;         /* Coins arrondis pour un aspect moderne */\n"
"}\n"
"\n"
"QTabBar {\n"
"    background-color: #ffffff;  /* Couleur de fond de la barre d'onglets (blanc) */\n"
"    padding: 0;                  /* Pas de padding pour occuper toute la largeur */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #f0f0f0;  /* Couleur de fond des onglets (gris clair) */\n"
"    color: black;                /* Couleur du texte des onglets */\n"
"    padding: 12px 20px;         /* Espacement autour du texte de l'onglet */\n"
"    border: none;                /* Pas de bordure entre les onglets */\n"
"    border-top-left-radius: 5px; /* Arrondi des coins sup\u00e9rieurs gauche */\n"
"    border-top-right-radius: 5px; /* Arrondi des coins sup\u00e9rieurs droit */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #d9d9d9"
                        ";  /* Couleur de fond de l'onglet s\u00e9lectionn\u00e9 (gris un peu plus fonc\u00e9) */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #d0d0d0;  /* Couleur de fond au survol de l'onglet (gris moyen) */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: #f0f0f0;  /* Couleur de fond des onglets non s\u00e9lectionn\u00e9s (gris clair) */\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: #ffffff;  /* Couleur de fond du contenu des onglets (blanc) */\n"
"    border: none;                /* Pas de bordure autour du contenu */\n"
"    border-radius: 0 0 5px 5px; /* Arrondi des coins inf\u00e9rieurs */\n"
"}")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gBox_action_banc_moteur = QGroupBox(self.tab_3)
        self.gBox_action_banc_moteur.setObjectName(u"gBox_action_banc_moteur")
        self.gBox_action_banc_moteur.setGeometry(QRect(20, 110, 311, 381))
        self.gBox_action_banc_moteur.setStyleSheet(u"QGroupBox {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    color: #2c3e50;\n"
"    font: bold 12px;\n"
"    background: transparent;\n"
"}")
        self.pb_visualiser_grandeurs = QPushButton(self.gBox_action_banc_moteur)
        self.pb_visualiser_grandeurs.setObjectName(u"pb_visualiser_grandeurs")
        self.pb_visualiser_grandeurs.setGeometry(QRect(55, 40, 201, 41))
        self.pb_visualiser_grandeurs.setStyleSheet(u"QPushButton {\n"
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
        self.pb_generer_caracteristique = QPushButton(self.gBox_action_banc_moteur)
        self.pb_generer_caracteristique.setObjectName(u"pb_generer_caracteristique")
        self.pb_generer_caracteristique.setGeometry(QRect(55, 100, 201, 41))
        self.pb_generer_caracteristique.setStyleSheet(u"QPushButton {\n"
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
        self.pb_parametrer_capteurs = QPushButton(self.gBox_action_banc_moteur)
        self.pb_parametrer_capteurs.setObjectName(u"pb_parametrer_capteurs")
        self.pb_parametrer_capteurs.setGeometry(QRect(55, 160, 201, 41))
        self.pb_parametrer_capteurs.setStyleSheet(u"QPushButton {\n"
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
        self.pb_piloter_frein_manuel = QPushButton(self.gBox_action_banc_moteur)
        self.pb_piloter_frein_manuel.setObjectName(u"pb_piloter_frein_manuel")
        self.pb_piloter_frein_manuel.setGeometry(QRect(55, 220, 201, 41))
        self.pb_piloter_frein_manuel.setStyleSheet(u"QPushButton {\n"
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
        self.pb_piloter_frein_profil = QPushButton(self.gBox_action_banc_moteur)
        self.pb_piloter_frein_profil.setObjectName(u"pb_piloter_frein_profil")
        self.pb_piloter_frein_profil.setGeometry(QRect(55, 280, 201, 41))
        self.pb_piloter_frein_profil.setStyleSheet(u"QPushButton {\n"
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
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(340, 110, 431, 381))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    color: #2c3e50;\n"
"    font: bold 12px;\n"
"    background: transparent;\n"
"}")
        self.pb_deconnecter = QPushButton(self.tab_3)
        self.pb_deconnecter.setObjectName(u"pb_deconnecter")
        self.pb_deconnecter.setGeometry(QRect(500, 530, 111, 31))
        self.pb_deconnecter.setStyleSheet(u"QPushButton {\n"
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
        self.pb_demarrer_cycle = QPushButton(self.tab_3)
        self.pb_demarrer_cycle.setObjectName(u"pb_demarrer_cycle")
        self.pb_demarrer_cycle.setGeometry(QRect(620, 30, 141, 41))
        self.pb_demarrer_cycle.setStyleSheet(u"QPushButton {\n"
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
        self.gBox_liste_essai = QGroupBox(self.tab_3)
        self.gBox_liste_essai.setObjectName(u"gBox_liste_essai")
        self.gBox_liste_essai.setGeometry(QRect(780, 110, 301, 381))
        self.gBox_liste_essai.setStyleSheet(u"QGroupBox {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 4px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    color: #2c3e50;\n"
"    font: bold 12px;\n"
"    background: transparent;\n"
"}")
        self.cBox_liste_essai = QComboBox(self.gBox_liste_essai)
        self.cBox_liste_essai.setObjectName(u"cBox_liste_essai")
        self.cBox_liste_essai.setGeometry(QRect(150, 30, 121, 31))
        self.cBox_liste_essai.setStyleSheet(u"QComboBox {\n"
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
        self.pb_selectionner_essai = QPushButton(self.gBox_liste_essai)
        self.pb_selectionner_essai.setObjectName(u"pb_selectionner_essai")
        self.pb_selectionner_essai.setGeometry(QRect(30, 30, 101, 31))
        self.pb_selectionner_essai.setStyleSheet(u"QPushButton {\n"
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
        self.tE_liste_essai = QTextEdit(self.gBox_liste_essai)
        self.tE_liste_essai.setObjectName(u"tE_liste_essai")
        self.tE_liste_essai.setGeometry(QRect(40, 90, 231, 211))
        self.pb_actualiser_liste_essai = QPushButton(self.gBox_liste_essai)
        self.pb_actualiser_liste_essai.setObjectName(u"pb_actualiser_liste_essai")
        self.pb_actualiser_liste_essai.setGeometry(QRect(90, 310, 91, 31))
        self.pb_actualiser_liste_essai.setStyleSheet(u"QPushButton {\n"
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
        self.pb_choisir_moteur = QPushButton(self.tab_3)
        self.pb_choisir_moteur.setObjectName(u"pb_choisir_moteur")
        self.pb_choisir_moteur.setGeometry(QRect(350, 30, 141, 41))
        self.pb_choisir_moteur.setStyleSheet(u"QPushButton {\n"
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
        self.l_moteur = QLabel(self.tab_3)
        self.l_moteur.setObjectName(u"l_moteur")
        self.l_moteur.setGeometry(QRect(390, 80, 351, 16))
        self.tab_administration.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab_administration.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lE_2AF = QLineEdit(self.tab_2)
        self.lE_2AF.setObjectName(u"lE_2AF")
        self.lE_2AF.setGeometry(QRect(517, 440, 91, 31))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.lE_2AF.setFont(font)
        self.lE_2AF.setStyleSheet(u"QLineEdit {\n"
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
        self.pb_valider_2AF = QPushButton(self.tab_2)
        self.pb_valider_2AF.setObjectName(u"pb_valider_2AF")
        self.pb_valider_2AF.setGeometry(QRect(510, 510, 101, 41))
        self.pb_valider_2AF.setStyleSheet(u"QPushButton {\n"
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
        self.l_reponse = QLabel(self.tab_2)
        self.l_reponse.setObjectName(u"l_reponse")
        self.l_reponse.setGeometry(QRect(620, 440, 391, 31))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 60, 171, 41))
        self.label.setMidLineWidth(1)
        self.qr_label = QLabel(self.tab_2)
        self.qr_label.setObjectName(u"qr_label")
        self.qr_label.setGeometry(QRect(438, 135, 261, 231))
        self.tab_administration.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 120, 510, 281))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 40, 113, 22))
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 100, 113, 22))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(100, 160, 113, 22))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(330, 40, 113, 22))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(330, 100, 113, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 40, 41, 21))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 100, 51, 21))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 160, 41, 21))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 40, 61, 21))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(255, 100, 71, 21))
        self.pb_valider_ajout_eleve = QPushButton(self.groupBox)
        self.pb_valider_ajout_eleve.setObjectName(u"pb_valider_ajout_eleve")
        self.pb_valider_ajout_eleve.setGeometry(QRect(320, 150, 121, 31))
        self.pb_valider_ajout_eleve.setStyleSheet(u"QPushButton {\n"
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
        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(580, 120, 510, 281))
        self.pb_choix_fichierCSV = QPushButton(self.groupBox_2)
        self.pb_choix_fichierCSV.setObjectName(u"pb_choix_fichierCSV")
        self.pb_choix_fichierCSV.setGeometry(QRect(30, 70, 161, 31))
        self.pb_choix_fichierCSV.setStyleSheet(u"QPushButton {\n"
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
        self.l_nomFichier = QLabel(self.groupBox_2)
        self.l_nomFichier.setObjectName(u"l_nomFichier")
        self.l_nomFichier.setGeometry(QRect(210, 70, 171, 31))
        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 261, 51))
        self.tab_administration.addTab(self.tab_4, "")

        self.retranslateUi(AppBancMot_prof)

        self.tab_administration.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AppBancMot_prof)
    # setupUi

    def retranslateUi(self, AppBancMot_prof):
        AppBancMot_prof.setWindowTitle(QCoreApplication.translate("AppBancMot_prof", u"Form", None))
        self.gBox_action_banc_moteur.setTitle(QCoreApplication.translate("AppBancMot_prof", u"Actions Banc Moteur", None))
        self.pb_visualiser_grandeurs.setText(QCoreApplication.translate("AppBancMot_prof", u"Visualiser Grandeurs", None))
        self.pb_generer_caracteristique.setText(QCoreApplication.translate("AppBancMot_prof", u"G\u00e9n\u00e9rer Caract\u00e9ristiques", None))
        self.pb_parametrer_capteurs.setText(QCoreApplication.translate("AppBancMot_prof", u"Param\u00e9trer Capteurs", None))
        self.pb_piloter_frein_manuel.setText(QCoreApplication.translate("AppBancMot_prof", u"Piloter Frein Manuel", None))
        self.pb_piloter_frein_profil.setText(QCoreApplication.translate("AppBancMot_prof", u"Piloter Frein Profils", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AppBancMot_prof", u"Informations", None))
        self.pb_deconnecter.setText(QCoreApplication.translate("AppBancMot_prof", u"D\u00e9connexion", None))
        self.pb_demarrer_cycle.setText(QCoreApplication.translate("AppBancMot_prof", u"D\u00e9marrer un cycle", None))
        self.gBox_liste_essai.setTitle(QCoreApplication.translate("AppBancMot_prof", u"Liste Essais R\u00e9alis\u00e9s", None))
        self.pb_selectionner_essai.setText(QCoreApplication.translate("AppBancMot_prof", u"S\u00e9lectionner", None))
        self.pb_actualiser_liste_essai.setText(QCoreApplication.translate("AppBancMot_prof", u"Actualiser", None))
        self.pb_choisir_moteur.setText(QCoreApplication.translate("AppBancMot_prof", u"Choisir un moteur ", None))
        self.l_moteur.setText(QCoreApplication.translate("AppBancMot_prof", u"TextLabel", None))
        self.tab_administration.setTabText(self.tab_administration.indexOf(self.tab_3), QCoreApplication.translate("AppBancMot_prof", u"Accueil", None))
        self.tab_administration.setTabText(self.tab_administration.indexOf(self.tab), QCoreApplication.translate("AppBancMot_prof", u"Aide", None))
        self.pb_valider_2AF.setText(QCoreApplication.translate("AppBancMot_prof", u"Valider", None))
        self.l_reponse.setText(QCoreApplication.translate("AppBancMot_prof", u"Reponse", None))
        self.label.setText(QCoreApplication.translate("AppBancMot_prof", u"Activation ou R\u00e9activation \n"
"de la double authentification ", None))
        self.qr_label.setText(QCoreApplication.translate("AppBancMot_prof", u"QRCODE", None))
        self.tab_administration.setTabText(self.tab_administration.indexOf(self.tab_2), QCoreApplication.translate("AppBancMot_prof", u"Param\u00e8tres", None))
        self.groupBox.setTitle(QCoreApplication.translate("AppBancMot_prof", u"Ajout manuel", None))
        self.label_3.setText(QCoreApplication.translate("AppBancMot_prof", u"Nom", None))
        self.label_4.setText(QCoreApplication.translate("AppBancMot_prof", u"Pr\u00e9nom", None))
        self.label_5.setText(QCoreApplication.translate("AppBancMot_prof", u"Classe", None))
        self.label_6.setText(QCoreApplication.translate("AppBancMot_prof", u"Identifiant", None))
        self.label_7.setText(QCoreApplication.translate("AppBancMot_prof", u"Mot de passe", None))
        self.pb_valider_ajout_eleve.setText(QCoreApplication.translate("AppBancMot_prof", u"Valider", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AppBancMot_prof", u"Importer un fichier csv", None))
        self.pb_choix_fichierCSV.setText(QCoreApplication.translate("AppBancMot_prof", u"Choisir un fichier CSV ", None))
        self.l_nomFichier.setText("")
        self.label_2.setText(QCoreApplication.translate("AppBancMot_prof", u"Ajouter un \u00e9l\u00e8ve manuellement ou en important \n"
"une liste d'\u00e9l\u00e8ves depuis un fichier CSV", None))
        self.tab_administration.setTabText(self.tab_administration.indexOf(self.tab_4), QCoreApplication.translate("AppBancMot_prof", u"Administration", None))
    # retranslateUi

