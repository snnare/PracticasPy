import threading
import time
import random


# EL ARGUMENTO OPCIONAL DA EL VALOR INICIAL PARA EL CONTADOR INTERNO
# CON VALOR DE 1
# SI EL VALOR DADO ES MENOR QUE 0, SE INCREMENTA ValueError

semaphore = threading.Semaphore(0)


def consumer():
    print('Consumidor esperando')
    # ADQUIERE EL SEMAFORO
    semaphore.acquire()
    # EL CONSUMIDOR TIENE ACCESO AL RECURSO COMPARTIDO
    print('Consumidor notifica: se ha consumido el intem numero %s '%item)

def producer():
    global item
    time.sleep(10)
    # CREA UN ITEM DE MANERA ALEATORIA
    item = random.randint(0,1000)
    print('Productor notifica: se ha producido el item numero %s '%item)
    # LUBERAR EL SEMAFORO, INCREMENTANDO EL CONTADOR INTERNO EN UNO
    # CUANDO ES CERO Y OTROO HILO ESTA ESPERANDOLO PARA HACERSE MAYOR QUE CERO
    # EL HILO DESPIERTA
    semaphore.release()

# PROGRAMA PRINCIPAL

def main():
    for i in range (0,5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    print("Programa Terminado")

if __name__ =="__main__":
    main()