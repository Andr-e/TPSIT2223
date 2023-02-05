from socket import socket, AF_INET, SOCK_STREAM
import sqlite3 as sq
import sys 


def chat_server(argv):
            
    with socket(AF_INET, SOCK_STREAM) as s:
        indirizzo =  argv[1]
        porta = argv[2]
        
        
        s.bind((indirizzo,int(porta)))
        s.listen()
        
        client, client_address = s.accept()
        running = True
        while running:
            msg = client.recv(4096)
            msg = msg.decode('utf-8')
            
            if msg == "signup":
                msg = client.recv(4096)
                msg = msg.decode('utf-8')
                dati = msg.split(';')
                nome, psw = dati
                nuovoUtente(nome,psw)
            
            elif msg == "login":
                msg = client.recv(4096)
                msg = msg.decode('utf-8')
                dati = msg.split(';')
                nome, psw = dati
                cercaUtente(nome, psw)               

def cercaUtente(nome, psw):
    conn = sq.connect("./Utenti.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM UTENTI WHERE Nome == (?) AND Password == (?)", (nome,psw))
    rows = curs.fetchall()
    for row in rows:
         print(row)
    
   
    

def nuovoUtente(nome,psw):
    conn = sq.connect("./Utenti.db")
    curs = conn.cursor()
    curs.execute("INSERT INTO UTENTI (Nome,Password) values (?,?)", (nome, psw))
    conn.commit()
    conn.close() 
    return conn 
        
if __name__ == "__main__":
    chat_server(sys.argv)