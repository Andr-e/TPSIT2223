from ast import mod
from base64 import encode
from http import client
import random
from socket import AF_INET, SOCK_STREAM, socket
import time
import config
from common import modexp,decode_big,encode_big



#def mypow(a,b,n):
   # return (a ** b) % n

def dh(client):
    # Genero segreto
    random.seed(int(time.time()))
    b = random.randint(1, config.P-2)

    # Genero numero pubblico
    gb = modexp(config.G, b, config.P)
    client.sendall(encode_big(gb))
    ga = decode_big(client.recv(4096))

    gab = modexp(ga, b, config.P)
    print(gab)
    return gab



def main():
    with socket(AF_INET, SOCK_STREAM)as s:
        s.bind(("0.0.0.0", 5001))
        s.listen()
        client,client_address = s.accept()
        dh(client)

   


if __name__ == "__main__":
    random.seed(int(time.time()))
    main()

