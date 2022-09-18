from socket import AF_INET, SOCK_DGRAM, socket

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        res = input("Inserisci l'ip di broadCast: ")
        while True:
            msg = input("Che messaggio vuoi mandare ?: ")
            #Codifica il messaggio in bytes
            msg = msg.encode('utf8')
            #Manda il messaggio al broadcast sulla porta 5000
            s.sendto(msg, (f"{res}", int(5000)))
          

       
if __name__ == "__main__":
    chatClient()


