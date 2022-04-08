import threading
import time
import os
from threading import Thread
from random import randint

# Definicion del Bloqueo (lock)

threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__ (self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Adquiere el Bloqueo (lock)
        threadLock.acquire()
        print("--> "+self.name+" corriendo y pertenece al proceso"+str(os.getpid()) + "\n")
        # Libera el Bloqueo (lock) en este punto
        threadLock.release()
        time.sleep(self.duration)
        print("--> "+self.name + " ha terminado \n")


def main():
    start_time = time.time()

    # Creacion de hilos 
    thread1 = MyThreadClass("Thread#1",randint(1,10))   
    thread2 = MyThreadClass("Thread#2",randint(1,10))
    thread3 = MyThreadClass("Thread#3",randint(1,10))    
    thread4 = MyThreadClass("Thread#4",randint(1,10))
    thread5 = MyThreadClass("Thread#5",randint(1,10))
    thread6 = MyThreadClass("Thread#6",randint(1,10))
    thread7 = MyThreadClass("Thread#7",randint(1,10))
    thread8 = MyThreadClass("Thread#8",randint(1,10))
    thread9 = MyThreadClass("Thread#9",randint(1,10))
    


    # Hilos corriendo
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    
    # Hilos juntandose

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # Finalizando
    print("FIN")
    
    # Tiempo de ejecuccion

    print("--- %s segundos ---"%(time.time() - start_time))

if __name__ == "__main__":
    main()

