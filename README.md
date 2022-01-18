# Proyecto: Sistema de detección y alarma ante fuga de gas
Repositorio con todo el código utilizado para el proyecto, así como los archivos de simulación, esquemáticos y capturas
# Descripción
Proceso de sensado de la concentración de GLP mediante el sensor de gas MQ-2 se convierte la información analógica a digital (ADC) donde se monitorea y envía a otro microcontrolador que lo envía  a su vez a una base de datos donde si se cumple cierta condición de concentración peligrosa de GLP se da una alerta mediante correo a el o los contactos configurados, adicionalmente de forma local se dan las alarmas sonoras y visuales. Además, con la aplicaicón movil se puede consultar por la información de concentración actual.
# Esquemáticos
ATMEGA328P | SENSOR(POTENCIOMETRO SIMULADO) | LCD | PUERTO COM | DRIVER PIC PARA LCD | TERMINAL VIRTUAL
![AT328P_esquematico](https://user-images.githubusercontent.com/64044895/149860108-1663c243-4245-4356-8d0f-81889e780796.png)
RASPBERRY PI 4 |  LED | BUZZER | PUERTO COM | TERMINAL VIRTUAL
![RPI4_esquematico](https://user-images.githubusercontent.com/64044895/149861173-3aea757d-aebf-48de-9c3b-5a134753a549.png)
ESQUEMÁTICO COMPLETO
![Esquematico_completo](https://user-images.githubusercontent.com/64044895/149861628-273a7632-fb6c-4cef-b2cc-2aabedec5619.png)
PCB
![PCB](https://user-images.githubusercontent.com/64044895/149861771-b11b0451-07d5-4136-aa02-7eb56bf832ba.png)
# Programas utilizados
- PROTEUS 8 PROFESSIONAL
- ATMEL STUDIO (PRODUCCION DE .HEX DE PRUEBA)
- VIRTUAL SERAL PORTS EMULATOR
# Indicaciones generales
- Serial a 9600 Baudios
- Frecuencia de 8 MHz
- Configuración estandar en modo UART
