# Modules
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import*
from funciones import*
from config import*

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
  prints("Concentracion: ")
  printsln(str(k1))
  payload = build_payload(VARIABLE_LABEL_1)
  print("[INFO] Attemping to send data")
  post_request(payload)
  print("[INFO] finished")
  sleep(0.1)  

# Command line execution
if __name__ == '__main__' :
 main()
