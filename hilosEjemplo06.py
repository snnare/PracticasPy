import threading
import time
import random

class Box:
    def __init__(self): 
        self.lock = threading.RLock()
        self.total_items = 0 

    def execute(self , value):
        with self.lock:
            self.total_items += value
    
    def add (self):
        with self.lock:
            self.execute(1)
    
    def remove (self):
        with self.lock:
            self.execute(-1)

def adder(box, items):
    print("Numero {} de items por AGREGAR \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items-=1
        print("SE AGREGO un item --> {} a los items por AGREGAR \n".format(items))



def remover(box, items):
    print("Numero {} de items por QUITAR \n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items-=1
        print("SE QUITO un item --> {} a los items por QUITAR \n".format(items))


def main():
    # items = 10
    box = Box()

    t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1,10))) 


    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ =="__main__":
    main()       