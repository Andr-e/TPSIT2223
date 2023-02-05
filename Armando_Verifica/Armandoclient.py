from socket import AF_INET, SOCK_STREAM, socket
from Armandoconfclient import Opzioni
import sys
import threading



def riceviComando():
    with socket(AF_INET,SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5005))
        s.listen()
        client,clientAddress = s.accept()
        utente = client.recv(7000).decode("utf8")
        messaggio = client.recv(7000).decode("utf8")
        print(f"{utente} scrive: {messaggio}")




    

def Client(args):
    opt = Opzioni(args[1], int(args[2]))
    with socket(AF_INET,SOCK_STREAM) as s:
        s.connect((opt.indirizzo, opt.porta))
        selezioneComando = input("salva o leggi ?: ")
        s.send(selezioneComando.encode("utf8").lower())
        if selezioneComando == "salva":
            commando = input("metti salva;nome;messaggio: ")
           # s.send(commando.encode())

        if selezioneComando == "leggi":
            riceviComando()

       


if __name__ == "__main__":
    Client(sys.argv)