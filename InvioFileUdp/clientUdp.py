from curses.ascii import SO
from socket import AF_INET, SOCK_DGRAM,socket

from packet import Packet

packet = Packet
def chatClient():
    with socket(AF_INET,SOCK_DGRAM) as s:
        with open("commedia.txt", "rb") as f:
            data = True
            while data:
                data = f.read(4096)
                s.sendto(packet(packet.GO_ON,data).to_bytes(), ("127.0.0.1", 5000))
            s.sendto(packet(packet.END_FILE,b"").to_bytes(), ("127.0.0.1", 5000))



if __name__ == "__main__":
    chatClient()