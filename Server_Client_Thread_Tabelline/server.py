from socket import socket
import threading
import time
import socket

def serverTabelline(conn, address):
    while True:
        msg = int(conn.recv(4096).decode())
        for i in range(1,11):
            calcolo = f"{msg} * {i} = {msg * i}"
            print(calcolo)
            conn.sendall(calcolo.encode())
        print("exit")
        conn.sendall("exit".encode())
      
            
           

       


        
      


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8001))
    server.listen()
    while True:
        conn,address = server.accept()
        t = threading.Thread(target=serverTabelline, args=(conn,address))
        t.start()
        
       

if __name__ == "__main__":
    main()