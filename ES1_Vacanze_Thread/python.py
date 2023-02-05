import threading

class ThreadIncrementa(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
    def run(self):
        self.x.incrementa()

class Increamenta(threading.Thread):
    def __init__(self, x ):
        threading.Thread.__init__(self)
        self.x = x
    def incrementa(self):
        for i in range(100000):
            self.x = self.x+ 1



if __name__ == "__main__":
    t = []
    # x è una classe di tipo incrementa
    x = Increamenta(0)
    for i in range(2000):
        nome = f"Processo numero {i}"
        t.append(ThreadIncrementa(x))


    for i in range(2000):
        t[i].start()

    for j in range(2000):
        t[j].join()


    print(x.x)

