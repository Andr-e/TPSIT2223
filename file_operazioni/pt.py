import socket
import sqlite3

def handle_signup(username, password):
    # salva nome utente e password nel database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

def handle_login(username, password):
    # controlla nome utente e password nel database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    if result is None:
        return False
    return result[0] == password

def handle_search(string):
    # cerca nomi utente nel database che contengono la stringa specificata
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT username FROM users WHERE username LIKE '%' || ? || '%'", (string,))
    result = c.fetchall()
    conn.close()
    return [r[0] for r in result]

def handle_client(client):
    while True:
        command = client.recv(1024).decode()
        if command == "signup":
            username = client.recv(1024).decode()
            password = client.recv(1024).decode()
            handle_signup(username, password)
            client.send("Registrazione completata".encode())
        elif command == "login":
            username = client.recv(1024).decode()
            password = client.recv(1024).decode()
            if handle_login(username, password):
                client.send("Accesso effettuato".encode())
            else:
                client.send("Accesso negato".encode())
        elif command == "search":
            string = client.recv(1024).decode()
            result = handle_search(string)
            client.send(str(result).encode())
        else:
            break
    client.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 1234))
    server.listen(5)
    while True:
        client, address = server.accept()
        print("Connessione da", address)
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
