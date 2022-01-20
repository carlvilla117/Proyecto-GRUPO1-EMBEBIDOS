import RPi.GPIO as GPIO
from wiringpi import Serial
from time import sleep

def init():
	TOKEN = "BBFF-bNW7tldWdGV51LuQPynZdwiNPUYtnG"  # Put your TOKEN here
	#Definición del dispositivo en Ubidots y la variable de concentracion
	DEVICE_LABEL = "Proyecto"  # Put your device label here 
	VARIABLE_LABEL_1 = "concentracion"  # Put your first variable label here
	baud = 9600
	ser  = Serial("/dev/serial0",baud)
	sleep(0.3)
