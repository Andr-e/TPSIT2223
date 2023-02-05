# (a ** b)% n
from re import S
import config
import random 

def modexp(a,b,n):
    acc=1
    while b>0:
        if b%2==1:
            acc=(acc*a)%n
        a=(a*a)%n
        b=b//2
    return acc
  
#Number -> String -> bytes
def encode_big(num):

    return str(num).encode("utf8")
#Bytes -> String -> Number 
def decode_big(s):
    return int(s.decode("utf8"))


#def dh(sock):
    # Genero segreto
    b = random.randint(1, config.P-2)
    
    # Genero numero pubblico
    sock.sendall(encode_big(gb))
    ga = decode_big(sock.rcv(4096))

    gab = modexp(ga, b, config.P)
    return gab
#



if __name__ == "__main__":
    assert(modexp(3,8,17)==16)
    

