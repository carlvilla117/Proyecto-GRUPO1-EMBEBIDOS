# Proyecto: Sistema de detección y alarma ante fuga de gas
Repositorio con todo el código utilizado para el proyecto, así como los archivos de simulación, esquemáticos y capturas de funcionamiento
# Descripción
Proceso de sensado de la concentración de GLP mediante el sensor de gas MQ-2 se convierte la información analógica a digital (ADC) donde se monitorea y envía a otro microcontrolador que lo envía  a su vez a una base de datos donde si se cumple cierta condición de concentración peligrosa de GLP se da una alerta mediante correo a el o los contactos configurados, adicionalmente de forma local se dan las alarmas sonoras y visuales. Además, con la aplicaicón movil se puede consultar por la información de concentración actual.
# Esquemáticos

## ATMEGA328P (PROTEUS)

![Proteus_Atmega328P](https://user-images.githubusercontent.com/89809182/150249223-a9a82c03-db6e-4e3f-96e3-ba627c54beee.JPG)

## RASPBERRY PI 4 (PROTEUS)

![Proteus_RaspberryPi4](https://user-images.githubusercontent.com/89809182/150249245-3df12490-9ab0-4cc7-9f15-3ff802ab8145.JPG)

## ESQUEMÁTICO COMPLETO (ATMEGA328P Y RASPBERRY PI4 JUNTOS)

![Componentes](https://user-images.githubusercontent.com/64044895/150248963-5c36fd1f-796c-4cfc-a283-6c30e9e1a3a8.png)

## PCB (PLACA DE CIRCUITO IMPRESO)

![PCB](https://user-images.githubusercontent.com/64044895/149861771-b11b0451-07d5-4136-aa02-7eb56bf832ba.png)

# MIT App Inventor

## DISEÑO DE LA APLICACIÓN

![App_inventor_designer](https://user-images.githubusercontent.com/89809182/150061427-fdcec9fe-dfcf-4401-9c76-4183adcef6c7.JPG)

## PROGRAMACIÓN EN BLOQUES DE LA APLICACIÓN

![App_inventor_Blocks](https://user-images.githubusercontent.com/89809182/150061423-c9ed1e6c-01f4-4edc-a861-1e3b16cb3298.JPG)

# Funcionamiento (Simulaciones)

## CONCENTRACION MENOR A 6000 [PPM]

![Concentración menor a 6000 PPM](https://user-images.githubusercontent.com/89809182/150261222-e74e3abd-7b20-440f-ae39-fa1d0ced272a.jpeg)

![Ubidots 2306  PPM](https://user-images.githubusercontent.com/89809182/150261230-77dc0609-df8b-4a9e-9d43-c7acd44c9675.jpeg)

## CONCENTRACION MAYOR A 6000[PPM]

![Concentración mayor a 6000  PPM](https://user-images.githubusercontent.com/89809182/150261287-d109bdff-7d34-4f57-8c65-efcc766124c4.jpeg)

![Ubidots 6910  PPM](https://user-images.githubusercontent.com/89809182/150261289-ff96cc27-d9ea-4ef0-9a27-08f55b1c2f41.jpeg)

![Notificación por correo](https://user-images.githubusercontent.com/89809182/150261568-79e4e3ec-fa7c-47d2-89f2-a8f6aafde9b0.jpeg)


# Programas utilizados
- PROTEUS 8 PROFESSIONAL
- ATMEL STUDIO (PRODUCCION DE .HEX DE PRUEBA)
- VIRTUAL SERAL PORTS EMULATOR
# Indicaciones generales
- Serial a 9600 Baudios
- Frecuencia de 8 MHz
- Configuración estandar en modo UART
