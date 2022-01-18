#include "config.c"
#include "i2c.c"
#include "lcd_i2c.c"
#include "i2c.c"
#include "uart.c"
#include "adc.c"


int main()
 { 
  serial_begin();
  i2c_init();
  i2c_start();
  i2c_write(0x70);
  lcd_init();
  DDRB = 0XFF; //PuertoB salida
  DDRC = 0X07; //Pines0,1 y 2 del puerto C como salida
  ADC_Init();
  interrupt_TIMER0_Init();
   while (1)
     {
	  int valor_adc=1.0f*(ADC)*9.775f;
      imprimir(valor_adc);
      //if(valor_adc>6000){PORTC |= (2<<1);} //se puede usar para tener la alarma de led y buzzer
      //lcd_cmd(0x80);
      //lcd_msg("Prueba para");
      //lcd_cmd(0xC3);
      //lcd_msg("I2C");


}
   return 0;
}

