## Multi-Threading with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(n):
    time.sleep(1)
    return f"Number: {n}"

## numbers = [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)
