int l1 = 11;
int l2 = 10;
int l3 = 12;
int l4 = 51;


void setup() {
  // put your setup code here, to run once:
  pinMode(l1, OUTPUT);
  pinMode(l2, OUTPUT);
  pinMode(l3, OUTPUT);
  pinMode(l4, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(l1, HIGH);
  digitalWrite(l2, HIGH);
  digitalWrite(l3, HIGH);
  digitalWrite(l4, HIGH);
  
  delay(250);      
           
  digitalWrite(l1, LOW);
  
  delay(250);       
         
  digitalWrite(l1, HIGH);
  digitalWrite(l2, LOW);
  
  delay(250);      
          
  digitalWrite(l1, LOW);
  
  delay(250);      
          
  digitalWrite(l1, HIGH);
  digitalWrite(l2, HIGH);
  digitalWrite(l3, LOW);
  
  delay(250);      
          
  digitalWrite(l1, LOW);
  
  delay(250);      
         
  digitalWrite(l1, HIGH);
  digitalWrite(l2, LOW);
  
  delay(250);     
           
  digitalWrite(l1, LOW);
  
  delay(250);     
           
  digitalWrite(l1, HIGH);
  digitalWrite(l2, HIGH);
  digitalWrite(l3, HIGH);
  digitalWrite(l4, LOW);
  
  delay(250);     
           
  digitalWrite(l1, LOW);
  
  delay(250);      
            
  digitalWrite(l1, HIGH);
  digitalWrite(l2, LOW);
  
  delay(250);     
            
  digitalWrite(l1, LOW);
  
  delay(250);   
             
  digitalWrite(l1, HIGH);
  digitalWrite(l2, HIGH);
  digitalWrite(l3, LOW);
  
  delay(250);     
         
  digitalWrite(l1, LOW);
  
  delay(250);     
            
  digitalWrite(l1, HIGH);
  digitalWrite(l2, LOW);
  
  delay(250);    
              
  digitalWrite(l1, LOW);
  
  delay(250);             

}
