def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Dijeljenje sa nulom nije dozvoljeno")
    return a/b

def power(a, b):
    if b < 0:
        raise ValueError("Negative exponents are not allowed")
    result = 1
    for _ in range(b):
        result *= a
    return result


def modulo(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a % b