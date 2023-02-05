
from socket import AF_INET, SOCK_STREAM,socket
from packet import Packet

packet = Packet
def chatClient():
    with socket(AF_INET,SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 5000))
        with open("commedia.txt", "rb") as f:
            data = True
            while data:
                data = f.read(4096)
                print("Letto")
                s.send(packet(packet.GO_ON,data).to_bytes())
            s.send(packet(packet.END_FILE,b"").to_bytes())
            print("Ho inviato il msg")



if __name__ == "__main__":
    chatClient()