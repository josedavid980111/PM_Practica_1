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
 Serial.print(cont2);
 Serial.print("     ");
Serial.print(cont1+s);
}
void receiveEvent(int howMany) {
  while (1< Wire.available()) {
    int D = Wire.read();
    int I = Wire.read();
    if(I==1 && D==0){
      if(cont1<255 && cont2==0){
        cont1 +=5;
      }
      if(cont2>0){
        cont2 -=5;
      }
      if(cont1>0 && cont2>0){
        cont1=0;
        cont2=0;
      }
    }else if (I==0 && D==1){
      if(cont2<255 && cont1==0){
        cont2 +=5;
      }
      if(cont1>0){
        cont1 -=5;
      }
      if(cont1>0 && cont2>0){
        cont1=0;
        cont2=0;
      }
    }else if (I==0 && D==0){
      
      if(cont1>0 && cont2>0){
        cont1=0;
        cont2=0;
      }
      else{
        cont1=255;
        cont2=255;
      }
    }
  }
}
