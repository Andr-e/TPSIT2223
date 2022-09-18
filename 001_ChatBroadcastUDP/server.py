from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET
#Quanti bit il nostro testo ha (massimi)
#bytes é un oggetto usato da python per gestire le str
#Se voglio trasferire una stinga la devo sempre transformare in bytes
BUFFER_SIZE = 1024

HOST = "0.0.0.0"
PORT = 5000
#Possibiltà
#LocalHost 127.0.0.1
#SOCK_DGRAM si intente il protocolo UDP


def scriviSuFile(msg):
    file = open("indirizzi.csv", "a")
    file.write(msg)
    file.write("\n")
    
    
    


def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:
        #Devo far capire che sto ascoltando dentro il bind metto dentro l'indirizzo da cui ascolo ed il secondo è la porta
        s.bind((HOST, PORT))
        s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
        print("server in ascolto")
        #Dichiaro una variabile msg per ricevere dati
        while True:
            msg = s.recvfrom(BUFFER_SIZE)
            #Decodifico da bytes a str
            msg = msg[0].decode("utf8")
            print(msg)
            scriviSuFile(msg)
            
           
       
      

       


 


    
#Questo if lo eseguiamo solo da terminale
if __name__ == "__main__":
    chatServer()