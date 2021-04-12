#include <ESP8266WiFi.h>;
#include <PubSubClient.h>;

int trigPin = 0;
int echoPin = 2;
long sure;
long uzaklik;

const char* ssid = ""; 				// wifi ssid
const char* password = "";			// wifi password
const char* mqtt_server = "broker.hivemq.com"; /// MQTT Broker
int mqtt_port = 1883;



WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup() { 
 Serial.begin(115200);
 // Start up the library
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin,INPUT);
  
 
 setup_wifi();
 client.setServer(mqtt_server, mqtt_port);
 client.setCallback(callback);

 Serial.println("Connected ");
 Serial.print("MQTT Server ");
 Serial.print(mqtt_server);
 Serial.print(":");
 Serial.println(String(mqtt_port)); 
 Serial.print("ESP8266 IP ");
 Serial.println(WiFi.localIP()); 
 Serial.println("Modbus RTU Master Online");

 //*****************
}

void setup_wifi() {

 delay(10);
 // We start by connecting to a WiFi network
 Serial.println();
 Serial.print("Connecting to ");
 Serial.println(ssid);

 WiFi.begin(ssid, password);

 while (WiFi.status() != WL_CONNECTED) {
 delay(500);
 Serial.print(".");
 }

 Serial.println("");
 Serial.println("WiFi connected");
 Serial.println("IP address: ");
 Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
 Serial.print("Message arrived [");
 Serial.print(topic);
 Serial.print("] ");
 for (int i = 0; i > length; i++) {
 Serial.print((char)payload[i]);
 }
 Serial.println();
 
}

void reconnect() {
 // Loop until we're reconnected
 while (!client.connected()) {
 Serial.print("Attempting MQTT connection...");
 // Attempt to connect
 if (client.connect("Temperature_Inside")) {

 Serial.println("connected");
 // client.subscribe("event");
 } else {
 Serial.print("failed, rc=");
 Serial.print(client.state());
 Serial.println(" try again in 5 seconds");
 // Wait 5 seconds before retrying
 delay(5000);
 }
 }
}
void loop() {
  //*****************
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);   
  sure = pulseIn(echoPin, HIGH); 
  uzaklik= sure /29.1/2;
  if(uzaklik > 200)
    uzaklik = 200;
  Serial.print("Uzaklik "); 
  Serial.print(uzaklik);
  Serial.println(" CM "); 
  delay(100);

  
 char temperaturenow [15];
 dtostrf(uzaklik,7, 3, temperaturenow); //// convert float to char 
 client.publish("TEMPERATURE", temperaturenow); /// send char 
 
 if (!client.connected()) {
 reconnect();

 }
 client.loop();

 delay(10000);
 
}
