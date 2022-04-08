
from threading import Thread, Condition
import time

items = []
condition = Condition()

class Consumer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()
        if (len(items) == 0):
            condition.wait()
            print('CONSUMIDOR NOTIFICA: No hay items que consumir')
        items.pop()
        print('CONSUMIDOR NOTIFICA: Se consumio 1 item')
        print('CONSUMIDOR NOTIFICA: Los items por consumir son ' + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0,20):
            time.sleep(2)
            self.consume()

class Producer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        condition.acquire()
        if (len(items) == 10):
            condition.wait()
            print('PRODUCTOR NOTIFICA: Los items producidos son ' + str(len(items)))
            print('PRODUCTOR NOTIFICA: Se detiene la producción')

        items.append(1)
        print('PRODUCTOR NOTIFICA: Total de items producidos ' + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0,20):
            time.sleep(0.5)
            self.produce()

def main():

    producer = Producer()
    consumer = Consumer()
        
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    
    main()