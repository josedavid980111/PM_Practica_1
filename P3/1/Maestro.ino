int botonD = 22;
int botonI = 23;
#include <Wire.h>

void setup() {
  
  pinMode(botonD, INPUT);
  pinMode(botonI, INPUT);
  Wire.begin(1);
  Serial.begin(9600);

}

String s = "\n";  
int valD, valI;

void loop() {
  Wire.beginTransmission(1); 
  valD = digitalRead(botonD);
  valI = digitalRead(botonI); 
  Serial.print(valI);
  Serial.print(valD+s);
  
  Wire.write(valD);
  Wire.write(valI); 
  Wire.endTransmission(); 
  delay(100);

}
