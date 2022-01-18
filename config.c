#include "config.h"

void imprimir(valor){
char valor_char[16];
sprintf(valor_char,"%d",valor);
serial_println_str(valor_char);
lcd_cmd(0x80);
lcd_msg("Concentracion: ");
lcd_cmd(0xC3);
lcd_msg(valor_char);
_delay_ms(1000);
}