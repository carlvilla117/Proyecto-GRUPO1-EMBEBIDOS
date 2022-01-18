#include "uart.h"

void serial_begin(){
	cli();
	float valor_UBBR0 = 0;
	UCSR0A=0b00000010;	//el bit 1 (U2X0) se pone en uno para duplicar la velocidad y poder utilizar frecuencias desde 1MHz
	UCSR0B=0b10011000;	//habilitar interrupcion por recepcion / transmision y recepcion habilitados a 8 bits
	UCSR0C=0b00000110;	//asincrono, sin bit de paridad, 1 bit de parada a 8 bits
	valor_UBBR0 = F_CPU/(16.0*BAUD);	//Definir la constante BAUD al inicio del codigo
        if(UCSR0A & (1<<U2X0)) valor_UBBR0 *= 2;
	UBRR0=valor_UBBR0 - 1;
        sei();
}

unsigned char serial_read_char(){
	if(UCSR0A&(1<<7)){  //si el bit7 del registro UCSR0A se ha puesto a 1
		return UDR0;    //devuelve el dato almacenado en el registro UDR0
	}
	else//sino
	return 0;//retorna 0
}

void serial_print_char(unsigned char caracter){
        if(caracter==0) return;
	while(!(UCSR0A&(1<<5)));    // mientras el registro UDR0 esta lleno espera
	UDR0 = caracter;            //cuando el el registro UDR0 esta vacio se envia el //caracter
}

void serial_print_str(char *cadena){	//cadena de caracteres de tipo char
	while(*cadena !=0x00){			//mientras el ultimo valor de la cadena sea diferente
							        //al caracter nulo
		serial_print_char(*cadena);	//transmite los caracteres de cadena
		cadena++;				//incrementa la ubicacion de los caracteres en cadena
								//para enviar el siguiente caracter de cadena
	}
}