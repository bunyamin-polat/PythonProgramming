## Multi-Processing
"""
Processes run in parallel, each with its own Python interpreter and memory space. 

This allows for true parallelism, making it suitable for CPU-bound tasks. For example, tasks like image processing, numerical simulations, and data analysis can benefit from multi-processing.

Parallel execution of tasks can significantly reduce the overall processing time, especially for compute-intensive operations. 

Multiple cores can be utilized effectively, leading to better performance and faster completion of tasks.

"""

import multiprocessing
import time

def square_numbers():
    for n in range(5):
        time.sleep(1)
        print(f"Square: {n * n}")


def cube_numbers():
    for n in range(5):
        time.sleep(1.5)
        print(f"Cube: {n * n * n}")
        

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    ## Create two processes
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()

    ## Start the processes
    process1.start()
    process2.start()

    ## Wait for the processes to finish
    process1.join()
    process2.join()

    finish_time = time.time()
    print(f"Total time taken: {finish_time - start_time:.2f} seconds")