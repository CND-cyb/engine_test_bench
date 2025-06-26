/*
# Titre : MQTT Acquisition, Publication des mesures et Contrôle Frein
# Auteur : TURKEL Ahmet Fatih
# Version : 28/04/2025
*/

#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <Arduino.h>
#include <math.h> // Pour sqrt()

// Déclarations des broches et constantes d'acquisition
const int entreeDynamoTachy = A0;    // Dynamotachymètre
const int entreeTension = A1;         // Tension moteur
const int entreeCourant = A2;         // Courant moteur
const int nombreEchantillons = 100;   // Nombre d'échantillons
const int intervalleEchantillonnage = 200; // Intervalle d'échantillonnage en µs

// PWM pour frein
const int LEDPin = 3; // Broche 3 pour le frein

// Définition des prescalers pour Timer3 (broche 3)
const byte PRESCALER_1_31kHz_TresRapide = 0b001;
const byte PRESCALER_8_4Hz = 0b010;
const byte PRESCALER_64_490Hz_Standard = 0b011;
const byte PRESCALER_256_122Hz = 0b100;
const byte PRESCALER_1024_30Hz_TresLent = 0b101;

// Choix prescaler pour frein
byte prescalerChoisi = PRESCALER_1024_30Hz_TresLent; // ~30 Hz pour frein

// Variables de mesures
float xTension = 0.0, xUDecal = 0.0, xUcarre = 0.0, xSommeValeursUcarre = 0.0;
float xCourant = 0.0, xIDecal = 0.0, xIcarre = 0.0, xSommeValeursIcarre = 0.0;
float xUeff = 0.0, xIeff = 0.0;
float xVitesse = 0.0, xCouple = 0.0;
int numeroMoteur = 1;

// Informations réseau et MQTT
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0F, 0x12, 0xDD };
IPAddress ip(192, 168, 2, 150);

const char* mqtt_broker = "192.168.2.100";
const char* mqtt_user = "bancmoteur";
const char* mqtt_password = "CestGenialCeBts2025";
const int mqttPort = 1883;
const char* topicMoteur = "Moteur/#";
const char* topicFrein = "Frein/CoeffA";

// Initialisation Ethernet et MQTT
EthernetClient ethClient;
PubSubClient client(ethClient);

// Prototypes
void setup_ethernet();
void reconnect();
void publishData();
void callback(char* topic, byte* payload, unsigned int length);

void setup() {
  Serial.begin(115200);
  pinMode(LEDPin, OUTPUT);

  Ethernet.begin(mac, ip);
  setup_ethernet();
  client.setServer(mqtt_broker, mqttPort);
  client.setCallback(callback);

  // Connexion au broker MQTT
  reconnect();

  // Réglage fréquence PWM sur broche 3 (Timer3)
  TCCR3B &= 0b11111000; // Effacer les bits CS32:CS30
  TCCR3B |= prescalerChoisi; // Appliquer le prescaler choisi
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Acquisition et affichage des mesures
  publishData();

  Serial.println("----- Mesures -----");
  Serial.print("Tension efficace (Ueff) : ");
  Serial.println(xUeff, 3);
  Serial.print("Courant efficace (Ieff) : ");
  Serial.println(xIeff, 3);
  Serial.print("Couple (Nm) : ");
  Serial.println(xCouple, 2);
  Serial.print("Vitesse moteur (tr/min) : ");
  Serial.println(xVitesse, 2);
  Serial.println("-------------------");

  delay(1000); // Attendre avant la prochaine acquisition
}

// Fonction appelée lors de la réception d'un message MQTT
void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (unsigned int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Réception MQTT [");
  Serial.print(topic);
  Serial.print("] : ");
  Serial.println(message);

  String topicStr = String(topic);

  if (topicStr == "Moteur/Numero") {
    int newNumero = message.toInt();
    if (newNumero >= 1 && newNumero <= 5) {
      numeroMoteur = newNumero;
      Serial.print("Changement de moteur : ");
      Serial.println(numeroMoteur);
    }
  } else if (topicStr == "Frein/CoeffA") {
    float pourcentage = message.toFloat();
    if (pourcentage >= 0 && pourcentage <= 100) {
      int pwm = map(pourcentage, 0, 100, 0, 255);

      // Ajuster la fréquence PWM
      TCCR3B &= 0b11111000;
      TCCR3B |= prescalerChoisi;

      // Appliquer le PWM
      analogWrite(LEDPin, pwm);

      Serial.print("Frein réglé à : ");
      Serial.print(pourcentage);
      Serial.println(" %");
    } else {
      Serial.println("Valeur frein invalide (0-100%)");
    }
  }
}

// Initialisation Ethernet avec fallback
void setup_ethernet() {
  Serial.println("Initialisation du réseau Ethernet...");
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Échec DHCP, attribution IP statique...");
    Ethernet.begin(mac, ip);
  }
  delay(1000);
  Serial.print("Adresse IP : ");
  Serial.println(Ethernet.localIP());
}

// Acquisition et publication des données sur MQTT
void publishData() {
  char msg[50];

  //// Mesure tension efficace (Ueff) ////
  xSommeValeursUcarre = 0.0;
  unsigned long startTimeTension = micros();
  for (int i = 0; i < nombreEchantillons; i++) {
    int valeur = analogRead(entreeTension);
    xTension = (valeur * 5.0) / 1023.0;
    xUDecal = xTension - 2.5;
    xUcarre = xUDecal * xUDecal;
    xSommeValeursUcarre += xUcarre;
    while (micros() - startTimeTension < (i + 1) * intervalleEchantillonnage) {}
  }
  xUeff = sqrt(xSommeValeursUcarre / nombreEchantillons);

  //// Mesure courant efficace (Ieff) ////
  xSommeValeursIcarre = 0.0;
  unsigned long startTimeCourant = micros();
  for (int i = 0; i < nombreEchantillons; i++) {
    int valeur = analogRead(entreeCourant);
    xCourant = (valeur * 5.0) / 1023.0;
    xIDecal = xCourant - 2.5;
    xIcarre = xIDecal * xIDecal;
    xSommeValeursIcarre += xIcarre;
    while (micros() - startTimeCourant < (i + 1) * intervalleEchantillonnage) {}
  }
  xIeff = sqrt(xSommeValeursIcarre / nombreEchantillons);

  //// Mesure vitesse moteur ////
  int valeurDynamo = analogRead(entreeDynamoTachy);
  float tensionDynamo = (valeurDynamo * 20.0) / 1023.0;
  xVitesse = tensionDynamo * 75; // Coefficient dépendant du modèle de dynamo

  //// Génération aléatoire d'un couple fictif ////
  xCouple = random(5, 15) + random(0, 100) / 100.0;

  // Publication MQTT
  dtostrf(xUeff, 6, 3, msg);
  client.publish("Moteur/Ueff", msg);
  delay(100);

  dtostrf(xIeff, 6, 3, msg);
  client.publish("Moteur/Ieff", msg);
  delay(100);

  dtostrf(xCouple, 6, 2, msg);
  client.publish("Moteur/C", msg);
  delay(100);

  dtostrf(xVitesse, 6, 2, msg);
  client.publish("Moteur/N", msg);
  delay(100);
}

// Reconnexion MQTT
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connexion au broker MQTT...");
    if (client.connect("MoteurClient", mqtt_user, mqtt_password)) {
      Serial.println("Connecté !");
      client.subscribe(topicMoteur);
      client.subscribe(topicFrein);
    } else {
      Serial.print("Échec, code erreur : ");
      Serial.println(client.state());
      Serial.println("Nouvelle tentative dans 2 secondes...");
      delay(2000);
    }
  }
}
