# Multiprocessing Pool 
from multiprocessing import Pool
import time
def f(n):
    sum = 0 
    for x in range(1000):
        sum += x*x
    return sum 
if __name__ == "__main__":
    t1 = time.time()
    p = Pool(processes=10) # processes limits number of processes
    result = p.map(f,range(100000))
    p.close()
    p.join()
    print("Pool took:",time.time()-t1)
    result = []
    t2 = time.time()
    for x in range(100000):
        result.append(f(x))
    print("Serial Processing took:",time.time()-t2)

    
