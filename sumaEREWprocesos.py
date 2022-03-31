import multiprocessing
import math


def executeProc(i,j,A):
    if (((2*j)%(math.pow(2,i))) == 0):
        A[2*j] = A[2*j] + A[((2*j)-((int) (math.pow(2,i-1))))]
        

def main():

    A = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(A)

    a = len(A)-1
    procesos = []
    log = int(math.log(a,2))
    for i in range(1,log+1):
        for j in range(1,(int)(a/2)+1):
            proc = multiprocessing.Process(target=executeProc,args=(i,j,A))
            procesos.append(proc)
            proc.start()
        
        for p in procesos:
            p.join()

        print(A)

if __name__ == '__main__':
    main()