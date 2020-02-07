int potenciometro = A0;
int fotosensor = A2;
int salida = A7;
double threshold = 500;
int porpot;
double fs;
//int brillo = 255;
//int pot=0;

void setup() {
  pinMode(potenciometro, INPUT);
  pinMode(fotosensor, INPUT);
  pinMode(salida, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int input = analogRead(fotosensor);
  threshold = ((analogRead (potenciometro)+400)/2);
  fs=analogRead(fotosensor);
  porpot=((threshold-200)/512)*100;
   if (input > threshold) {
      digitalWrite(salida, HIGH);
      //pot = analogRead (potenciometro) / 4; 
      //brillo = pot/4;
      //analogWrite(salida, brillo);
   }
   else {
      digitalWrite(salida, LOW);
   }
   
   Serial.print("Valor potenciometro:  ");
   Serial.print(porpot);
   Serial.println("%");
   Serial.println();
   Serial.print("Valor Fotosensor:  ");
   Serial.print((fs/1024)*100);
   Serial.println("%");
   delay(1000);

}
