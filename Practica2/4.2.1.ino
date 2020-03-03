int cont=0;
void setup()
{
Serial.begin(9600);
DDRB = DDRB | B00000011; // Data Direction Register B: Inputs 0-6, Output 7

DDRD &= ~(1 << DDD1);
PORTD |= (1 << PORTD1);
EICRA |= (1 << ISC10);
EIMSK |= (1 << INT1);
sei();


}
ISR(INT1_vect){

cont=cont+1;

Serial.print(cont);
  asm (

"sbi 0x05,0x01 \n\t"
"call tiempo2 \n\t"
"cbi 0x05,0x01 \n\t");

}

void loop(){

asm (


"inicio: \n\t" 

"sbi 0x05,0x00 \n\t"
"call tiempo \n\t"
"cbi 0x05,0x00 \n\t"
"call tiempo \n\t"


"jmp main \n\t"



"tiempo: \n\t"
"LDI r22, 40 \n\t"
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


"tiempo2: \n\t"
"LDI r22, 10 \n\t"
"LOOP_6: \n\t"
"LDI r21, 255 \n\t"
"LOOP_5: \n\t"
"LDI r20, 255 \n\t"
"LOOP_4: \n\t"
"DEC r20 \n\t"
"BRNE LOOP_4 \n\t"
"DEC r21 \n\t"
"BRNE LOOP_5 \n\t"
"DEC r22 \n\t"
"BRNE LOOP_6 \n\t"
"ret \n\t"
);

}
