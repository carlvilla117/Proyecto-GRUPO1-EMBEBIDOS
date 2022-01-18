#include "adc.h"

void interrupt_TIMER0_Init(){
	cli();
	TCCR0B = 0b101; //PREESCALADOR 1024
	TIMSK0 = 1; //HB TIMER POR DESBORDAMIENTO
	sei();
	TCNT0 = 12; //250ms
}
void ADC_Init(){
	ADMUX  = 0b01000011; //vcc, aref, adc0
	ADCSRA = 0b10101111; //activo no iniciado, automatico,interrupcion terminacion, prescalador 128
	ADCSRB = 0b00000100; //debordamiento timer0
}

ISR(TIMER0_OVF_vect){
	TCNT0 = 12;
}

ISR(ADC_vect){
	PORTB = ADCL;
	PORTC = ADCH;
}