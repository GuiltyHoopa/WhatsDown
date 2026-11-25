import socket
import threading

HOST = "127.0.0.1"
PORT = 676767

def ricevi_messaggio(s):
    while True:
        try:
            messaggio = s.recv(1024).decode()
            if not messaggio:
                break
            print(messaggio)
        except:
            print("\003[91mConnessione persa con il server\003[0m]")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect( (HOST, PORT) )

# avvio il thread

threading.Thread( target=ricevi_messaggio , args=(s,), daemon=True ).start()

while True:
    try:
        ...
    except KeyboardInterrupt:
        #CTRL + C
        ...


