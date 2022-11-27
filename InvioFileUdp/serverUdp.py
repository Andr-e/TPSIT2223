from socket import AF_INET,SOCK_DGRAM,socket

from packet import Packet
file = []
def chatServer():
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))
        while True:
            msg = s.recvfrom(7000)
            packet = Packet.from_bytes(msg[0])
            if packet.status  == packet.GO_ON:
                file.append(packet.data)
            if packet.status == packet.END_FILE:
                with open("file.html", "wb") as f:
                    f.write(b"".join(file))
                    break




if __name__ == "__main__":
    chatServer()


                

