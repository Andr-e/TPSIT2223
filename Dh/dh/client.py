from ast import arg
from base64 import decode, encode
from mimetypes import common_types
import random
from socket import AF_INET, SOCK_STREAM, socket
import config
import time
import sys
from common import modexp,encode_big,decode_big
from http import server

#def mypow(a,b,n):
 #   return (a ** b) % n




def dh(s):
     
        # Genero segreto
        random.seed(2*int(time.time()))
        a = random.randint(1, config.P-2)

        # Genero numero pubblico
        #ga = mypow(config.G, a, config.P)
        ga = modexp(config.G, a, config.P)
        s.sendall(encode_big(ga))
        

       # gb = int(input("Inserire l'altro numero: "))
        gb = decode_big(s.recv(4096))

        #gab = mypow(gb, a, config.P)
        gab  = modexp(gb, a, config.P)

        print(gab)
        return gab

def main(args):
    a =  random.seed(2*int(time.time()))
    if len(args) < 3:
        print("Usage: {args[0]} ip port")
    address = (args[1],int(args[2]))
    with socket(AF_INET,SOCK_STREAM) as s:
        s.connect(address)
        gab = dh(s)

  



if __name__ == "__main__":
    main(sys.argv)
  