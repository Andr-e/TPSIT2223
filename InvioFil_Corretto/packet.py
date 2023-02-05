class Packet:
    INIZIO = 0
    CONTINUA = 1
    FINE = 2

    def __init__(self,blocco, status):
        self.blocco = blocco
        self.status =status


    def to_bytes(self):
        #Per lo stato ci dedico 1 bytes per la lunghezza 2 bytes
        return b"".join([self.status.to_bytes(1,"big"),len(self.status).to_bytes(2,"big"),self.blocco,
        ])
    @staticmethod
    def from_bytes(buffer):
        #buffer --- > array di bytes
        status = int.from_bytes(buffer[:1],"big")
        lung = int.from_bytes(buffer[1:3], "big")
        blocco = buffer[3:3 + lung]
        return Packet(blocco, status)




if __name__ == "__main__":
    pk0 = Packet(b"ciao", False)
    print(pk0.to_bytes())
    
        


        