void setup()
{
DDRB = DDRB | B00111111; // Data Direction Register B: Inputs 0-6, Output 7
}

void loop()
{

asm (
"inicio: \n\t" 

"sbi 0x05,0x00 \n\t"
"sbi 0x05,0x05 \n\t"

"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"

"cbi 0x05,0x00 \n\t"
"sbi 0x05,0x01 \n\t"

"call tiempo \n\t"

"cbi 0x05,0x01 \n\t"
"cbi 0x05,0x05 \n\t"


"sbi 0x05,0x03 \n\t"
"sbi 0x05,0x02 \n\t"

"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"

"cbi 0x05,0x03 \n\t"
"sbi 0x05,0x04 \n\t"

"call tiempo \n\t"

"cbi 0x05,0x04 \n\t"
"cbi 0x05,0x02 \n\t"












"jmp main \n\t"



"tiempo: \n\t"
"LDI r22, 80 \n\t"
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
