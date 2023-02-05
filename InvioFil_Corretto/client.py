from ast import Pass
from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet

BUF_SIZE = 10
def inviaFile(s,dest):
    with open("myFile.txt", "rb") as f:
        finito = False
        socket.sendto((b"", Packet.INIZIO.from_bytes()),dest)
        while  not finito:
           
            dati  = f.read(BUF_SIZE)
            if not dati:
                socket.sendto(Packet(dati,Packet.CONTINUA).to_bytes(), dest)
            else:
                finito = True
        socket.sendto(Packet(dati,Packet.FINE).to_bytes(), dest)



def Client():
    dest = ("127.0.0.1", 5000)
    with socket(AF_INET,SOCK_DGRAM) as s:
        inviaFile(s, dest)


if __name__ == "__main__":
    Client()