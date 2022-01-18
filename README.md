# Proyecto: Sistema de detección y alarma ante fuga de gas
Repositorio con todo el código utilizado para el proyecto, así como los archivos de simulación, esquemáticos y capturas
# Descripción
Proceso de sensado de la concentración de GLP mediante el sensor de gas MQ-2 se convierte la información analógica a digital (ADC) donde se monitorea y envía a otro microcontrolador que lo envía  a su vez a una base de datos donde si se cumple cierta condición de concentración peligrosa de GLP se da una alerta mediante correo a el o los contactos configurados, adicionalmente de forma local se dan las alarmas sonoras y visuales. Además, con la aplicaicón movil se puede consultar por la información de concentración actual.
# Esquemáticos
ATMEGA328P | SENSOR(POTENCIOMETRO SIMULADO) | LCD | PUERTO COM | DRIVER PIC PARA LCD | TERMINAL VIRTUAL
![AT328P_esquematico](https://user-images.githubusercontent.com/64044895/149860108-1663c243-4245-4356-8d0f-81889e780796.png)
RASPBERRY PI 4 | LED | BUZZER | PUERTO COM | TERMINAL VIRTUAL
![RPI4_esquematico](https://user-images.githubusercontent.com/64044895/149861173-3aea757d-aebf-48de-9c3b-5a134753a549.png)
ESQUEMÁTICO COMPLETO
![Esquematico_completo](https://user-images.githubusercontent.com/64044895/149861628-273a7632-fb6c-4cef-b2cc-2aabedec5619.png)
PCB
![PCB](https://user-images.githubusercontent.com/64044895/149861771-b11b0451-07d5-4136-aa02-7eb56bf832ba.png)

APP INVENTOR | DESIGNER

![App_inventor_designer](https://user-images.githubusercontent.com/89809182/150012112-42acdf84-63c2-400d-af1d-cd9faa53ce94.JPG)

APP INVENTOR | BLOCKS

![App_inventor_Blocks](https://user-images.githubusercontent.com/89809182/150012134-a0aa6f81-e5d7-41d8-aea8-da9b0e6593b6.JPG)
DIAGRAMA INICIAL ATMEGA328P | RASPBERRY PI 4 | CONCENTRACION<6000[PPM]
![Diagrama inicial](https://user-images.githubusercontent.com/89809182/150015160-7ec2cca8-eb9f-4c6d-846e-64f4e1262321.JPG)
SIMULACION ATMEGA328P | RASPBERRY PI 4 | CONCENTRACION<6000[PPM]
![Concentración menor a 6000PPM](https://user-images.githubusercontent.com/89809182/150015173-232650d2-fece-4630-9c1b-69e33936eeec.JPG)
SIMULACION UBIDOTS | CONCENTRACION<6000[PPM]
![Concentración menor a 6000PM_Ubidots](https://user-images.githubusercontent.com/89809182/150015181-61ab72ba-8f38-44f7-a210-7c3009040323.JPG)
SIMULACION ATMEGA328P | RASPBERRY PI 4 | CONCENTRACION>6000[PPM]
![Concentración mayor a 6000PPM](https://user-images.githubusercontent.com/89809182/150015201-dcc64291-88a9-4197-98a0-30593e8ffed9.JPG)
SIMULACION UBIDOTS | CONCENTRACION>6000[PPM]
![Concentración mayor a 6000PPM_Ubidots](https://user-images.githubusercontent.com/89809182/150015207-cb5864f7-2c5d-4a97-a088-a84fb342cb35.JPG)

NOTIFICACION POR CORREO

![Notificacion por correo](https://user-images.githubusercontent.com/89809182/150012136-9c262b6f-c1e9-4105-a284-812075471498.JPG)


# Programas utilizados
- PROTEUS 8 PROFESSIONAL
- ATMEL STUDIO (PRODUCCION DE .HEX DE PRUEBA)
- VIRTUAL SERAL PORTS EMULATOR
# Indicaciones generales
- Serial a 9600 Baudios
- Frecuencia de 8 MHz
- Configuración estandar en modo UART
