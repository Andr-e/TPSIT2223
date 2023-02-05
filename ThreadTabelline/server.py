import threading
import socket
import time
import keyboard

def serverFun(conn,address,msg):
    running = True
    while running:
        
        for i in range(11):
            n = msg*i
            s = (f"{msg} * {i} = {n} \n")
            conn.sendall(s.encode())
            print(s)
        print("Fine tabellina \n")
        running = False
        
def main():
    print("Server in ascolto \n")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    running = True
    while running:
        conn, address = server.accept()        
        msg = conn.recv(4096).decode()
        msg = int (msg)
        t = threading.Thread(target=serverFun, args=(conn,address,msg))
        t.start()

if __name__ == "__main__":
    main()