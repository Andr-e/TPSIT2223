from socket import AF_INET, SOCK_STREAM,socket

from packet import Packet
file = []
def chatServer():
    with socket(AF_INET,SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))
        s.listen()
        client,clientAddress = s.accept()
        while True:
            msg = client.recv(7000)
            packet = Packet.from_bytes(msg)
            if packet.status  == packet.GO_ON:
                file.append(packet.data)
                print(packet.status)
            if packet.status == packet.END_FILE:
                with open("file.html", "wb") as f:
                    f.write(b"".join(file))
                    break




if __name__ == "__main__":
    chatServer()


                

