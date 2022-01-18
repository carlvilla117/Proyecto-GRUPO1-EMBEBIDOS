#include "config.h"

void serial_begin();
unsigned char serial_read_char();
void serial_print_char(unsigned char caracter);
void serial_print_str(char *cadena);