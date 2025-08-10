from logger import logging

def add_numbers(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

logging.info("Adding function called")
add_numbers(5, 10)
