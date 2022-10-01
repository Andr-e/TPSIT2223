from socket import AF_INET, SOCK_DGRAM, socket
from struct import pack
#Importo la classe Packet da un altro file, situato nella stessa cartella
import sys
sys.path.insert(1, '/Applications/Python/TPSIT2223.old')
from packet import Packet
def chatClient(username, res):
    with socket(AF_INET, SOCK_DGRAM) as s:
       
        while True:
            msg = input("Che messaggio vuoi mandare: ")
            #Codifica il messaggio in bytes
            pkt0 = Packet(username, msg)
            pkt1 = pkt0.to_bytes()
            
            #Manda il messaggio al broadcast sulla porta 5000
            s.sendto(pkt1, (res, int(5000)))   
if __name__ == "__main__":
    username = input("Qual'è il tuo nome: ")
    res = input("Inserisci l'ip di broadCast: ")
    chatClient(username, res)