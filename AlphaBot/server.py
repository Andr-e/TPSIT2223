from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket
import time
from AlphaBot import AlphaBot 
a = AlphaBot()
def chatServer():
    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0",5000))
        s.listen()
        client,clientAddress=s.accept()
        while True:
            a.stop()
        
            msg=client.recv(1024).decode("utf8")
            if(msg=="avanti"):
                print(msg)
                a.forward()
                time.sleep(1)
            if(msg=="indietro"):
                print(msg)
                a.backward()
                time.sleep(1)
            if(msg=="sinistra"):
                print(msg)
                a.left()
                time.sleep(1)
            if(msg=="destra"):
                print(msg)
                a.right()
                time.sleep(1)

if __name__ == "__main__":
    chatServer()