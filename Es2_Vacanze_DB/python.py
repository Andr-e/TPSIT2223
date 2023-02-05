import sqlite3 as sq

def inserisciUtenti(arg1, arg2):
    #Riempire il db da python
    conn = sq.connect("UTENTI.db")
    cur = conn.cursor()
   
    cur.execute("INSERT into UTENTI (Nome,Password) values (?,?)",(arg1,arg2))
    conn.commit()
    conn.close()

def main():
    name = input("Metti un nome: ")
    password = input("Metti una password: ")
    inserisciUtenti(name,password)

if __name__ == "__main__":
    main()