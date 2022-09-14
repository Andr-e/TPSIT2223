from socket import AF_INET, SOCK_DGRAM, socket

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        msg = "hello world"
        msg = msg.encode('utf8')

        s.sendto(msg, ("192.168.98.255", 5000))

if __name__ == "__main__":
    chatClient()