import threading
import time


def funzione(num):
    print(f"Partenza del {num}",threading.current_thread().name)
    print("elabora")
    time.sleep(2)
    print(f"Finito lavoro {num}",threading.current_thread().name)


# La funzione join: Non fa andare avanti il programma finchè non finisce il primo thred,
# poi va anditi con il secondo,
# poi il terzo.

# Start: Fa partire il Thread, (Non abbiamo garazie sul ordine della pratenza dei thread)
# Per riferimento al thread si riferisce alle variabili t,q
def main():
    t = threading.Thread(target = funzione,args=(1,),name = "Primo")
    t.start()
    t.join()
    q = threading.Thread(target = funzione,args=(2,), name =  "Secondo")
    q.start()
    q.join()
    funzione(3)


if __name__ == "__main__":
    main()