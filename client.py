import socket
import threading

HOST = "127.0.0.1"
PORT = 676767

def ricevi_messaggio():
    ...

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect( (HOST, PORT) )

# avvio il thread

threading.Thread( target=ricevi_messaggio , args=(), daemon=True ).start()

while True:
    try:
        ...
    except KeyboardInterrupt:
        #CTRL + C


