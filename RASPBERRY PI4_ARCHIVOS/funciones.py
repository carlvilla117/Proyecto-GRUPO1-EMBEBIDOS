import os
import socket
import requests
from wiringpi import Serial
from time import sleep

baud = 9600
ser  = Serial("/dev/serial0",baud)
sleep(0.3)
myip = socket.gethostbyname(socket.gethostname())
print (myip)

def recibir(echo = True):
 data = ""
 while True:
  input = ser.getchar()
  if echo:
   ser.putchar(input)
  if input == "\r":
   return (data)
  data += input
 sleep(0.2)
  
def printsln(menss):
 ser.puts(menss+"\r")
 sleep(0.2)

def prints(menss):
 ser.puts(menss)
 sleep(0.2)

def servidor():
 Request = None

 class RequestHandler_httpd(BaseHTTPRequestHandler):
   def do_GET(self):
    global Request

    messagetosend = bytes('Solicitando',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]

    #print(Request)
    if Request == 'soldatos':
      print('Los datos han sido enviados a la app')
      valor=int(recibir())
      firebase.put("/Dato","/dato1",valor)
 
def build_payload(variable_1):
    value_1 = int(recibir()) #Recibo el dato de concentracion
    print ("CONECTADO...")  
    payload = {variable_1: value_1}
    return payload

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True
