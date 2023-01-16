import time 
import threading
def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube',n*n*n)
arr = [2,3,8,9]
time_  = time.time() 
t0= threading.Thread(target=calc_square,args=(arr,))
t1= threading.Thread(target=calc_cube,args=(arr,))
# start the thread 
t0.start()
t1.start()
# wait until it is done
t1.join()
t1.join()
print("done in: ",time.time()-time_)
print("Ha... I am done with my work now!")