# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accueil.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1073, 646)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff; /* Fond blanc */\n"
"}")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(1, 1, 1141, 671))
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
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
        self.pb_visualiser_grandeurs.setGeometry(QRect(40, 40, 201, 41))
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
        self.pb_generer_caracteristique.setGeometry(QRect(40, 100, 201, 41))
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
        self.pb_parametrer_capteurs.setGeometry(QRect(40, 160, 201, 41))
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
        self.pb_piloter_frein_manuel.setGeometry(QRect(40, 220, 201, 41))
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
        self.pb_piloter_frein_profil.setGeometry(QRect(40, 280, 201, 41))
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
        self.gB_informations = QGroupBox(self.tab_3)
        self.gB_informations.setObjectName(u"gB_informations")
        self.gB_informations.setGeometry(QRect(340, 110, 431, 381))
        self.gB_informations.setStyleSheet(u"QGroupBox {\n"
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
        self.pb_deconnexion = QPushButton(self.tab_3)
        self.pb_deconnexion.setObjectName(u"pb_deconnexion")
        self.pb_deconnexion.setGeometry(QRect(500, 530, 111, 31))
        self.pb_deconnexion.setStyleSheet(u"QPushButton {\n"
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
        self.pb_selection_essai = QPushButton(self.gBox_liste_essai)
        self.pb_selection_essai.setObjectName(u"pb_selection_essai")
        self.pb_selection_essai.setGeometry(QRect(30, 30, 101, 31))
        self.pb_selection_essai.setStyleSheet(u"QPushButton {\n"
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
        self.pb_actualiser = QPushButton(self.gBox_liste_essai)
        self.pb_actualiser.setObjectName(u"pb_actualiser")
        self.pb_actualiser.setGeometry(QRect(90, 310, 91, 31))
        self.pb_actualiser.setStyleSheet(u"QPushButton {\n"
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
        self.l_moteur.setGeometry(QRect(380, 80, 351, 16))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
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
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(510, 680, 101, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 18px;\n"
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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gBox_action_banc_moteur.setTitle(QCoreApplication.translate("Form", u"Actions Banc Moteur", None))
        self.pb_visualiser_grandeurs.setText(QCoreApplication.translate("Form", u"Visualiser Grandeurs", None))
        self.pb_generer_caracteristique.setText(QCoreApplication.translate("Form", u"G\u00e9n\u00e9rer Caract\u00e9ristiques", None))
        self.pb_parametrer_capteurs.setText(QCoreApplication.translate("Form", u"Param\u00e9trer Capteurs", None))
        self.pb_piloter_frein_manuel.setText(QCoreApplication.translate("Form", u"Piloter Frein Manuel", None))
        self.pb_piloter_frein_profil.setText(QCoreApplication.translate("Form", u"Piloter Frein Profils", None))
        self.gB_informations.setTitle(QCoreApplication.translate("Form", u"Informations", None))
        self.pb_deconnexion.setText(QCoreApplication.translate("Form", u"D\u00e9connexion", None))
        self.pb_demarrer_cycle.setText(QCoreApplication.translate("Form", u"D\u00e9marrer un cycle", None))
        self.gBox_liste_essai.setTitle(QCoreApplication.translate("Form", u"Liste Essais R\u00e9alis\u00e9s", None))
        self.pb_selection_essai.setText(QCoreApplication.translate("Form", u"S\u00e9lectionner", None))
        self.pb_actualiser.setText(QCoreApplication.translate("Form", u"Actualiser", None))
        self.pb_choisir_moteur.setText(QCoreApplication.translate("Form", u"Choisir un moteur ", None))
        self.l_moteur.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Accueil", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Aide", None))
        self.pb_valider_2AF.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.l_reponse.setText(QCoreApplication.translate("Form", u"Reponse", None))
        self.label.setText(QCoreApplication.translate("Form", u"Activation ou R\u00e9activation \n"
"de la double authentification ", None))
        self.qr_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Param\u00e8tres", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Quitter", None))
    # retranslateUi

