from socket import AF_INET, SOCK_STREAM, socket
import sys
BUF_SIZE = 4096


class Opzioni:
    def __init__(self,portaServer, host, porta):
        self.portaServer = int(portaServer)
        self.host = host
        self.porta = int(porta)
    def get_socket(self):
        return self.host,self.porta


def richiedi_dati(sock,percorso):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(sock[0], sock[1])
        s.sendall(f"GET {percorso}.json HTTP/1.0\n\n").encode("utf8")
        data = s.recv(BUF_SIZE)
        data2 = s.recv(BUF_SIZE)
        return data + data2

        #data = True
       # dati = []
      #  while data !=None:
       #     
        #    if data != None:
                
       #         dati.append(data)
      #  dati = b"".join(dati)
      #  print(dati)


    pass    
def chatServer(args):
    opt = Opzioni(args[1], args[2],args[3])
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0",opt.portaServer))
        s.listen()
        while True:
            client,clientAddress = s.accept()
            #Qua viene fatto un solo recv anche se sembra dentro un while
            #Questo è un while di accettazione della connessione
            #Quindi lo eseguo solo 1 volta il recv, perchè ogni volta aspetta una connessione
            data = client.recv(BUF_SIZE)
            data = data.decode("utf8")
            campi = data.split(" ")
            data = richiedi_dati(opt.get_socket,campi[1])
            client.sendall(data)
            print(data)

     
    
    

if __name__ == "__main__":
    chatServer(sys.argv)
