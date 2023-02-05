from socket import SOCK_DGRAM, AF_INET,socket
from packet import Packet

def scriviFile(file):
    with open("ciao.txt", "wb") as f:
        f.write(file)

def Server():
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))
        pezzi = []
        while True:
            msg, da = s.recvfrom(8095)
            pkt = Packet.from_bytes(msg)

            if pkt.status == Packet.INIZIO:
                pezzi = []
            if pkt.status  == Packet.CONTINUA:
                pezzi.append(pkt.blocco)
            else:
                scriviFile(b"".join(pezzi))





if __name__ == "__main__":
    Server()
