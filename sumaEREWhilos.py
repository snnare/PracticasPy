import threading
import math
import time


def executeThread(i,j,A):
    if(((2*j)%(math.pow(2,i))) == 0):
        A[2*j] = A[2*j] + A[((2*j)-((int) (math.pow(2,i-1))))] 
    time.sleep(2)


def main():
    A = [0,1,1,1,1,1,1,1,1]
    print(A)

    a = len(A)-1
    threads = []
    log = int(math.log(a,2))
    for i in range (1,log+1):
        for j in range (1,(int)(a/2)+1):
            thread = threading.Thread(target=executeThread, args=(i,j,A))
            threads.append(thread)
            thread.start()

        for hilo in threads:
            hilo.join()
        
        print(A)

if __name__ == '__main__':
    main()