def inizio_Fine(fun):
    def wrapper():
        print("inizio")
        fun()
        print("fine")
    return wrapper


@inizio_Fine
def ciao():
    print("ciao")

ciao = inizio_Fine(ciao)
@inizio_Fine
def hello(): 
    print("Hello")



if __name__ == "__main__":
    ciao()
    hello()