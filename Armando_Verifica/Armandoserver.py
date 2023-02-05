from socket import AF_INET,SOCK_STREAM,socket
import threading
from Armandoconfclient import Opzioni


def leggiFile(file):
    with open(file, "r") as f:
        dati = f.readline()
        dati = dati.split(",")
        return dati

def inviaComando(arg1,arg2,arg3):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((arg3))
        s.send(arg1.encode(),arg2.encode())
       

class ThreadConnessione(threading.Thread):
    def __init__(self,conn,clientAddress):
        threading.Thread.__init__(self)
        self.conn = conn
        self.clientAddress = clientAddress
    def run(self):
        listaUtenti = []
        listaMsg = []
        while True:
             msg = self.conn.recv(7000)
            
             dato =msg.decode("utf8")
             print(dato)
             if dato == "salva":
                 msg1 = self.conn.recv(7000).decode("utf8")
                 print(msg1)
                 print("ciao qui va")
                # listaUtenti.append(msg1.split(";")[1])
                # listaMsg.append(msg1.split(";")[2])
                 #print(listaUtenti)

                 if dato == "leggi":
                    inviaComando(listaUtenti.pop(), listaMsg.pop(),self.clientAddress)

def Server(arg):
    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((arg[0], int(arg[1])))
        s.listen()
        client,clientAddress = s.accept()
        
        

        threadConnessione = ThreadConnessione(client,clientAddress)
        threadConnessione.start()
        
           
               

                
            



if __name__ == "__main__":
    sock = leggiFile("Armandoconfserver.txt")
    Server(sock)