def add(a, b):
    """Return sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return product of two numbers."""
    return a * b

def divide(a, b):
    """Return quotient of two numbers, raises ValueError if b = 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def factorial(n):
    """Return factorial of n (non-negative integer)."""
    if n < 0:
        raise ValueError("Negative number not allowed.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def average(numbers):
    """Return average of a list of numbers."""
    if not numbers:
        raise ValueError("Empty list.")
    return sum(numbers) / len(numbers)

def max_in_list(numbers):
    """Return the maximum number in a list."""
    if not numbers:
        raise ValueError("Empty list.")
    return max(numbers)

def min_in_list(numbers):
    """Return the minimum number in a list."""
    if not numbers:
        raise ValueError("Empty list.")
    return min(numbers)

def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent
