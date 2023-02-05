from socket import socket, AF_INET, SOCK_STREAM
import sys
def chat_client(argv):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((argv[1], int(argv[2])))
        running = True
        while running:
            msg = input('Fai login o signup ?:')
            s.send(msg.encode())
            if msg == "signup":
                utente = input("nome utente: ")
                psw = input("password: ")
                dati = utente + ";" + psw
                print(dati)
                s.send(dati.encode())
            elif msg == "login":
                utente = input("nome utente: ")
                psw = input("password: ")
                dati = utente + ";" + psw
                
                s.send(dati.encode())
if __name__ == "__main__":
    chat_client(sys.argv)