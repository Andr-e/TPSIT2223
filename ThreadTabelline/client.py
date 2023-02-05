import threading
import socket
import time

def main():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    op = input("Inserisci un numero: ")
    client.sendall(op.encode())
    while True:
        ans = client.recv(4096).decode()
        print(f"{ans}")

if __name__ == "__main__":
    main()