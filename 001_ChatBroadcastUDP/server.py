from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET

BUFFER_SIZE = 1024

mystr = "ciao" # str
# bytes

HOST = "0.0.0.0"
PORT = 5000
# possibilità
# localhost 127.0.0.1 


def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        while True:
            msg = s.recvfrom(BUFFER_SIZE)
            msg = msg[0].decode('utf8')
            print(msg)

if __name__ == "__main__":
    chatServer()