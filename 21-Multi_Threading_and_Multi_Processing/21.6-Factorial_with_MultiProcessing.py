"""
Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, involve significant computational work. 
Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.
"""

import multiprocessing
import math
import time
import sys

## Increase maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

def factorial(n):
    print(f"Calculating factorial of {n}...")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    
    numbers = [5000, 6000, 7000, 8000]
    
    start_time = time.time()

    ## Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    end_time = time.time()
    print("Factorials calculated:", results)
    print(f"Time taken: {end_time - start_time} seconds")