def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def divide(a, b):
    """Return the division of two numbers, handle division by zero."""
    if b == 0:
        return "Division by zero is not allowed"
    return a / b