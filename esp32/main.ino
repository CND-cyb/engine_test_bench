/*
# Titre : Application ESP32 Ecran
# Auteur : Benjamin
# Version : 11/03/2025
*/

#include "EasyNextionLibrary.h"  // Bibliothèque de gestion de l'écran Nextion
#include "WiFi.h"                // Bibliothèque pour la connexion WiFi
#include "PubSubClient.h"        // Bibliothèque pour le protocole MQTT

// Définition des broches de communication série avec l'écran Nextion
#define RXD2 16
#define TXD2 17

// Variables de mesure moteur
long int couleurTexte;
float xTensionInt=0, xCourantInt=0, xVitesseInt=0, xCoupleInt=0, xPUtileInt=0;

// Variables de caractéristiques nominales du moteur
float valTensionCara=0, valCourantCara=0, valVitesseCara=0, valCoupleCara=0, valPUCara=0;
String typeMoteur;

// Paramètres de connexion WiFi et MQTT
const char* ssid = "banc_moteur_btsciel";
const char* password = "CestGenialCeBts2025";
const char* mqtt_broker = "192.168.2.100";
const char* mqtt_user = "bancmoteur";
const char* mqtt_password = "CestGenialCeBts2025";

// Objets pour la gestion du WiFi, MQTT et de l'écran Nextion
WiFiClient espClient;
PubSubClient client(espClient);
EasyNex myNex(Serial2);

void setup() {
  // Initialisation du port série pour le debug
  Serial.begin(115200);
  Serial.println("Démarrage du programme");
  // Initialisation de la communication avec l'écran Nextion
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2);
  // Connexion au réseau WiFi
  setup_wifi();
  // Configuration du serveur MQTT
  client.setServer(mqtt_broker, 1883);
  client.setCallback(callback);
  // Connexion au broker MQTT
  Serial.println("Tentative de connexion au broker MQTT...");
  while (!client.connected()) {
    String client_id = "ESP32Client";
    if (client.connect(client_id.c_str(), mqtt_user, mqtt_password)) {
      Serial.println("ESP32 connecté au Broker MQTT!");
    } else {
      Serial.print("Erreur connexion MQTT ");
      Serial.print(client.state());
      Serial.println(" - reconnexion dans 2 secondes.");
      delay(2000);
    }
  }
  // Abonnement aux topics MQTT
  client.subscribe("Moteur/#");
  client.subscribe("Caracteristique/#");
  // Mise à jour initiale de l'écran
  updateCaracteristique();
  updateValeur();
}

// Fonction appelée à chaque réception d’un message MQTT
void callback(char* topic, byte* payload, unsigned int length) { 
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);

  // Analyse du topic reçu et mise à jour des variables correspondantes
  if (String(topic) == "Moteur/Ueff") {
    xTensionInt = message.toFloat()*10;
    updateValeur();
  } else if (String(topic) == "Moteur/Ieff") {
    xCourantInt = message.toFloat()*100;
    updateValeur();
  } else if (String(topic) == "Moteur/C") {
    xCoupleInt = message.toFloat()*10;
    updateValeur();
  } else if (String(topic) == "Moteur/N") {
    xVitesseInt = message.toFloat();
    updateValeur();
  } else if (String(topic) == "Caracteristique/Unom") {
    valTensionCara = message.toFloat()*10;
    updateCaracteristique();
  } else if (String(topic) == "Caracteristique/Inom") {
    valCourantCara = message.toFloat()*100;
    updateCaracteristique();
  } else if (String(topic) == "Caracteristique/Cnom") {
    valCoupleCara = message.toFloat()*10;
    updateCaracteristique();
  } else if (String(topic) == "Caracteristique/Nnom") {
    valVitesseCara = message.toFloat();
    updateCaracteristique();
  } else if (String(topic) == "Caracteristique/PUnom") {
    valPUCara = message.toFloat();
    updateCaracteristique();
  } else if (String(topic) == "Caracteristique/Type") {
    typeMoteur = message;
    updateCaracteristique();
  } 
}

// Connexion au réseau WiFi
void setup_wifi() {
  Serial.print("Connexion à ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connecté!");
  Serial.print("Adresse IP : ");
  Serial.println(WiFi.localIP());
}

// Reconnexion au broker MQTT si nécessaire
void reconnect() {
  while (!client.connected()) {
    Serial.print("Tentative de connexion MQTT...");
    String client_id = "ESP32Client-";
    client_id += String(random(0xffff), HEX); // ID client aléatoire
    
    if (client.connect(client_id.c_str(), mqtt_user, mqtt_password)) {
      Serial.println("connecté");
      client.subscribe("Moteur/#");
      client.subscribe("Caracteristique/#");
    } else {
      Serial.print("échec, rc=");
      Serial.print(client.state());
      Serial.println(" nouvelle tentative dans 5 secondes");
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();                // Gère la réception MQTT
  myNex.NextionListen();       // Écoute les événements de l'écran Nextion

  // Calcul de la puissance utile
  xPUtileInt = (xCoupleInt/10) * (((2*3.14)*xVitesseInt)/60);
}

// Mise à jour des valeurs mesurées sur l'écran
void updateValeur() {
  const char* tabUnite[] = {"xTension", "xCourant", "xCouple", "xPUtile","xVitesse"};
  float tabValeurs[] = {xTensionInt, xCourantInt, xCoupleInt, xPUtileInt, xVitesseInt};
  float moteur[] = {valTensionCara, valCourantCara, valCoupleCara, valPUCara, valVitesseCara};

  for (int i = 0; i <= 4; i++) {
    myNex.writeNum(tabUnite[i] + String(".val"), tabValeurs[i]);
    // Changement de couleur en rouge si dépassement de 95% des caractéristiques
    if (tabValeurs[i] >= (moteur[i] * 95 / 100) && moteur[i]!=0) {
      couleurTexte = 63488; // rouge
    } else {
      couleurTexte = 2047; // bleu
    }
    myNex.writeNum(tabUnite[i] + String(".pco"), couleurTexte);
    myNex.writeNum(tabUnite[i] + String("Unite.pco"), couleurTexte);
  }
}

// Mise à jour des caractéristiques nominales du moteur sur l'écran
void updateCaracteristique() {
  const char* tabUnite[] = {"xCaraTension", "xCaraCourant", "xCaraCouple", "xCaraPuissance", "xCaraVitesse"};
  float moteur[] = {valTensionCara, valCourantCara, valCoupleCara, valPUCara, valVitesseCara};
  for (int i = 0; i <= 4; i++) {
    myNex.writeNum(tabUnite[i] + String(".val"), moteur[i]);
  }
  myNex.writeStr("labType.txt", typeMoteur);
}

// Fonction déclenchée par une interaction avec l’écran (ex : appui sur un bouton)
void trigger0() {
  int pourcentageFrein = myNex.readNumber("xConsigne.val");
  if (pourcentageFrein <= 100 && pourcentageFrein >= 0) {
    Serial.print("Frein : ");
    Serial.println(pourcentageFrein);
    client.publish("Frein/Profil", "0");
    String coeffA = String(pourcentageFrein);
    client.publish("Frein/CoeffA", coeffA.c_str());
  }
}
