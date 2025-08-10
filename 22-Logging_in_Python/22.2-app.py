import logging

## Logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"), # Log to a file
        logging.StreamHandler() # Log to console
    ],
    force = True
)

logger = logging.getLogger("CalculatorApp")

def add(x, y):
    result = x + y
    logger.debug(f"Adding {x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    logger.debug(f"Subtracting {x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    logger.debug(f"Multiplying {x} * {y} = {result}")
    return result

def divide(x, y):
    try:
        result = x / y
        logger.debug(f"Dividing {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

add(5, 3)
subtract(5, 3)
multiply(5, 3)
divide(5, 0)
