# Proyecto: Sistema de detección y alarma ante fuga de gas
Repositorio con todo el código utilizado para el proyecto, así como los archivos de simulación, esquemáticos y capturas de funcionamiento
# Descripción
Proceso de sensado de la concentración de GLP mediante el sensor de gas MQ-2 se convierte la información analógica a digital (ADC) donde se monitorea y envía a otro microcontrolador que lo envía  a su vez a una base de datos donde si se cumple cierta condición de concentración peligrosa de GLP se da una alerta mediante correo a el o los contactos configurados, adicionalmente de forma local se dan las alarmas sonoras y visuales. Además, con la aplicaicón movil se puede consultar por la información de concentración actual.
# Esquemáticos

ATMEGA328P (PROTEUS)

![Proteus_Atmega328P](https://user-images.githubusercontent.com/89809182/150249223-a9a82c03-db6e-4e3f-96e3-ba627c54beee.JPG)

RASPBERRY PI 4 (PROTEUS)

![Proteus_RaspberryPi4](https://user-images.githubusercontent.com/89809182/150249245-3df12490-9ab0-4cc7-9f15-3ff802ab8145.JPG)

ESQUEMÁTICO COMPLETO (ATMEGA328P Y RASPBERRY JUNTOS)

![Componentes](https://user-images.githubusercontent.com/64044895/150248963-5c36fd1f-796c-4cfc-a283-6c30e9e1a3a8.png)

PCB (PLACA DE CIRCUITO IMPRESO)

![PCB](https://user-images.githubusercontent.com/64044895/149861771-b11b0451-07d5-4136-aa02-7eb56bf832ba.png)

# MIT App Inventor

DISEÑO DE LA APLICACIÓN

![App_inventor_designer](https://user-images.githubusercontent.com/89809182/150061427-fdcec9fe-dfcf-4401-9c76-4183adcef6c7.JPG)

PROGRAMACIÓN EN BLOQUES DE LA APLICACIÓN

![App_inventor_Blocks](https://user-images.githubusercontent.com/89809182/150061423-c9ed1e6c-01f4-4edc-a861-1e3b16cb3298.JPG)

# Funcionamiento (Simulaciones)


SIMULACION ATMEGA328P | RASPBERRY PI 4 | CONCENTRACION<6000[PPM]

SIMULACION UBIDOTS | CONCENTRACION<6000[PPM]

SIMULACION ATMEGA328P | RASPBERRY PI 4 | CONCENTRACION>6000[PPM]

SIMULACION UBIDOTS | CONCENTRACION>6000[PPM]


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










