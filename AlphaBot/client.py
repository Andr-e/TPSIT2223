from socket import AF_INET, SO_BROADCAST, SOCK_STREAM, socket

def chatClient(ip, port):
    with socket (AF_INET, SOCK_STREAM) as s:
        s.connect((ip, port))
        while True:
         dir = input("Inserisci direzione: ")
         s.send(dir.encode('utf-8'))
         tempo = input("Inserisci tempo: ")
         s.send(tempo.encode('utf-8'))

if __name__ == "__main__":
    ip = input("Inserisci ip: ")
    port = int(input("Inserisci porta: "))
    chatClient(ip, port)