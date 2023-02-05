from doctest import DocFileCase
from errno import EEXIST
from pydoc import plain
from this import d
from unittest import removeResult
from winreg import REG_REFRESH_HIVE, DeleteKey


class Packet:

    def __init__(self,comando,utente,messaggio):
        self.comando = comando
        self.utente = utente
        self.messaggio = messaggio

    def encode(self):
        risultato = self.comando + ";" + self.utente + ":" + self.messaggio
        return risultato.encode()
    
    @staticmethod
    
    def decode(buffer):
        strPacchetto = buffer.decode()
        campi = strPacchetto.split(";")
        comando = campi[0]
        utente = campi[1]
        messaggio = campi[2]
        return Packet(comando,utente, messaggio)
    
