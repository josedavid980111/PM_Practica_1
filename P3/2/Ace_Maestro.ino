int X=A0;
int Y=A1;
int Z=A2;
#include <Wire.h>
void setup() {
  pinMode(Y,INPUT);
  Wire.begin(1);
  Serial.begin(9600);
}
int x1, y1, z1, y2, giro, aux1, aux2;
double girod, giroi;
String s = "\n"; 
void loop() {
  x1=analogRead(X);
  y1=analogRead(Y);
  z1=analogRead(Z);
  y2=y1-333;
  if(y2>0){
    giroi=0;
    if(y2>90){
      girod=255;
    }
    else if(y2<=90){
      girod=((double)y2/90)*255;
    }
  }
  else{
    girod=0;
    if(y2<-90){
      giroi=255;
    }
    else{
      giroi=((double)(-y2)/90)*255;
    }
  }
  aux1=girod;
  aux2=giroi;
  Serial.print(y2);
  Serial.print("              ");
  Serial.print(giroi);
  Serial.print("   ");
  Serial.print(girod+s);
  Wire.beginTransmission(1); 
  Wire.write(aux1);
  Wire.write(aux2);
  Wire.endTransmission();
}
