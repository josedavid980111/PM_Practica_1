int derecho = 2;
int izquierdo =3;
#include <Wire.h>
void setup() {
  pinMode(derecho, OUTPUT);
  pinMode(izquierdo, OUTPUT);
  Wire.begin(1);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);

}
String s = "\n";  
int cont1,cont2;
void loop() {
  analogWrite(derecho, cont1);
 
 analogWrite(izquierdo, cont2);
 delay(100);
}

void receiveEvent(int howMany) {
  while (1< Wire.available()) {
    int girod=Wire.read();
    int giroi=Wire.read();
    Serial.print(giroi);
    Serial.print("   ");
    Serial.print(girod+s);
    cont1=girod;
    cont2=giroi;
  }
}
