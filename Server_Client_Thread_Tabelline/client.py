import socket

def main(arg):
    cl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cl.connect(("127.0.0.1", 8001))
    cl.sendall(arg.encode())
    while True:
        risp = cl.recv(4096).decode()
        print(risp)
        

    







if __name__ == "__main__":
    inputNum = input("Inserisci un numero : ")
    main(inputNum)