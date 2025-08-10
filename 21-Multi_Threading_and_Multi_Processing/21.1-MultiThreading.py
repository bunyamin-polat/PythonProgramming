## Multi-Threading and Multi-Processing

"""Program: A program is a set of instructions that a computer executes to perform a specific task.

Process: A process is an instance of a program that is being executed. It contains the program code and its current activity. Each process has its own memory space and system resources.

Thread: A thread is the smallest unit of processing that can be scheduled by an operating system. Threads are used to perform tasks concurrently within a process, sharing the same memory space but having their own execution stack.

Memory Segments:
- Code Segment: Contains the compiled program code.
- Data Segment: Contains global and static variables.
- Heap Segment: Contains dynamically allocated memory.
- Stack Segment: Contains local variables and function call information.
- Register Segment: Contains the CPU registers used by the process.

Separate Memory Spaces

Each process has its own memory space, which means that the memory segments of one process are isolated from those of another. 

This separation helps prevent issues like memory corruption and makes it easier to manage resources.

I/O Requirements
- Each process has its own I/O resources, such as file handles and network connections.
- I/O operations are typically blocking, meaning a process will wait for an I/O operation to complete before continuing.
- Multi-threading can help improve I/O performance by allowing other threads to run while one thread is waiting for I/O.
"""

### Multi-Threading
"""
When we use multi-threading?
1. To improve application responsiveness by offloading long-running tasks to background threads.
2. To perform concurrent I/O operations, allowing other threads to run while one thread is waiting for I/O.
3. To utilize multiple CPU cores for parallel processing, improving overall performance.
"""

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}", sep="\n")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(2)
        print(f"Letter: {letter}", sep="\n")

## Creating Threads

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

start_time = time.time()

## Starting Threads
thread1.start()
thread2.start()

## Waiting for Threads to Complete
thread1.join()
thread2.join()

finished_time = time.time()
print(f"Finished in {finished_time - start_time} seconds")
