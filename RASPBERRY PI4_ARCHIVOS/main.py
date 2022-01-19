# Modules
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import*
from firebase import firebase
from funciones import*
from config import*

firebase = firebase.FirebaseApplication('https://proyecto-dimensiones-default-rtdb.firebaseio.com/', None)

init()



# Main function
def main () :
# Infinite loop
 while True:
  mensaje = recibir()
  k1 = 0
  try:
   k1 = int(mensaje)
  except:
   print("error")
   pass
  sleep(0.1)
  #printsln("Concentracion: ")
  prints("Concentracion: ")
  printsln(str(k1))

  if k1 <=6000:
    GPIO.output(led1,False)
    GPIO.output(buzz,False)
  elif k1 >6000:
    GPIO.output(led1,True)
    GPIO.output(buzz,True)

  payload = build_payload(VARIABLE_LABEL_1)
  print("[INFO] Attemping to send data")
  post_request(payload)
  print("[INFO] finished")
  sleep(10)  
  try:
   servidor()
  except(KeyboardInterrupt,SystemExit):
   print ("BYE")

# Command line execution
if __name__ == '__main__' :
 main()