def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    
def exponentiate(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Return the least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def fraction_to_decimal(numerator, denominator):
    """Convert a fraction to its decimal representation."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return numerator / denominator

def main():
    print("Addition: ", add_numbers(10, 5))
    print("Subtraction: ", subtract_numbers(10, 5))
    print("Multiplication: ", multiply_numbers(10, 5))
    print("Division: ", divide_numbers(10, 5))
    print("Fibonacci(10): ", fibonacci(10))
    print("Exponentiation: ", exponentiate(2, 3))
    print("Factorial(5): ", factorial(5))
    print("GCD(48, 18): ", gcd(48, 18))
    print("LCM(4, 5): ", lcm(4, 5))
    print("Fraction to Decimal (1/3): ", fraction_to_decimal(1, 3))