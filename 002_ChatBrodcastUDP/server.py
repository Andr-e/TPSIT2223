
from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET
import sys
sys.path.insert(1, '/Applications/Python/TPSIT2223.old')
from packet import Packet
#Quanti bit il nostro testo ha (massimi)
#bytes é un oggetto usato da python per gestire le str
#Se voglio trasferire una stinga la devo sempre transformare in bytes
BUFFER_SIZE = 1024
#Possibiltà
#LocalHost 127.0.0.1
#SOCK_DGRAM si intente il protocolo UDP

def scriviSuFile(pkt0):
    file = open("indirizzi.csv", "a")
    file.write(f"{pkt0.username}: {pkt0.message}")
    file.write("\n")

def chatServer(HOST, PORT):
    with socket(AF_INET, SOCK_DGRAM) as s:
        #Devo far capire che sto ascoltando dentro il bind metto dentro l'indirizzo da cui ascolo ed il secondo è la porta
        s.bind((HOST, PORT))
        s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
        print("server in ascolto")
        #Dichiaro una variabile msg per ricevere dati
        while True:
            msg = s.recvfrom(BUFFER_SIZE)
            #Decodifico da bytes a str
            pkt0 = Packet.from_bytes(msg[0])
           
            scriviSuFile(pkt0)
            
           
       
      

       


 


    
#Questo if lo eseguiamo solo da terminale
if __name__ == "__main__":
    HOST = input("Inserisci l'host: ")
    PORT = int(input("Inserisci la porta: "))
    chatServer(HOST, PORT)