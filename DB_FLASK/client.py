
import json
from os import access
from flask import request
HOST = "http://127.0.0.1:5000"


def getPercorsi():
    percorsi = request.get(HOST+ "/api/v1/percorsi")
    #In questo modo gestiamo le GET
    percorsi.content()
    print(percorsi)

def creaPercorso():
    data = {"nome":"quadrato"}
    request.post(HOST+ "/api/v1/percorsi",json = data  )
   
    
def main(): 
    getPercorsi()
    creaPercorso()


if __name__ == "__main__":
    main()