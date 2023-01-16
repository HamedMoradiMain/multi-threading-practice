import time
import multiprocessing
square_results = []
def calc_square(numbers):
    global square_results
    for n in numbers:
        print(f"square {n*n}")
        square_results.append(n*n)
    print(f"within a process: result {square_results}")
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    t = time.time()
    # start the processes 
    p1.start()
    # wait until processes finish successfully!
    p1.join()
    print(f"results {square_results}")
    print(f"Done! at {time.time()-t} secs")
    