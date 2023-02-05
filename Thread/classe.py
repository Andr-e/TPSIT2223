from socket import socket
import threading
import time
import socket

class MyClassThread(threading.Thread):
    def __init__(self,conn):
        # Riga 9: Richiamo il costruttore della classe Genitore Thread
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        while True:
            self.msg = conn.recv(4096).decode()
            if (msg == "ESC"):
                conn.close()
            else:
                try:
                    ris = eval(msg)
                    print(ris)
                    #conn.sendall(ris.encode())

                except:
                    print("Non corretto")
                    pass
           

       


        
      


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8002))
    server.listen()
    while True:
        conn,address = server.accept()
        t = threading.Thread(target=serverFun, args=(conn,address))
        t = MyClassThread(conn)
        t.start()
        
       

if __name__ == "__main__":
    main()