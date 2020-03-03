//contador
int contador = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  cli();
  
  DDRD &= ~(1 << DDD1);
  PORTD |= (1 << PORTD1);
  EICRA |= (1 << ISC10);
  EIMSK |= (1 << INT1);
  sei();
  DDRB = DDRB | B00100000; 
  }
  ISR(INT1_vect)
  {
    contador=contador+1;
    Serial.println(contador);
   }


void loop() {
  // put your main code here, to run repeatedly:
  asm (
    "inicio: \n\t" 
    "sbi 0x05,0x05 \n\t"
    "call tiempo \n\t"
    "cbi 0x05,0x05 \n\t"
    "call tiempo \n\t"
    "jmp inicio \n\t"
    
    "tiempo: \n\t"
    "LDI r22, 20 \n\t"
    "LOOP_3: \n\t"
    "LDI r21, 255 \n\t"
    "LOOP_2: \n\t"
    "LDI r20, 255 \n\t"
    "LOOP_1: \n\t"
    "DEC r20 \n\t"
    "BRNE LOOP_1 \n\t"
    "DEC r21 \n\t"
    "BRNE LOOP_2 \n\t"
    "DEC r22 \n\t"
    "BRNE LOOP_3 \n\t"
    "ret \n\t"
    );
}
