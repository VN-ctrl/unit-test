import pytest

from main import (
    add_numbers as add,
    subtract_numbers as subtract,
    multiply_numbers as multiply,
    divide_numbers as divide,
    fibonacci,
    exponentiate,
    factorial,
    gcd,
    lcm,
    fraction_to_decimal,
)


def test_add():
    """Verify addition works for positive, negative, and zero."""
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Verify subtraction handles positive and negative results."""
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5


def test_multiply():
    """Verify multiplication works with positive, negative, and zero operands."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0


def test_divide():
    """Verify division works with normal operands."""
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3


def test_divide_by_zero():
    """Ensure divide() raises ValueError when dividing by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_fibonacci_value():
    """Verify fibonacci returns expected value for n=10."""
    # According to main.py: fibonacci(1)=0, fibonacci(2)=1, fibonacci(10)=34
    assert fibonacci(10) == 34


def test_fibonacci_invalid():
    """Verify fibonacci raises for non-positive n."""
    with pytest.raises(ValueError):
        fibonacci(0)


def test_exponentiate_and_fraction():
    """Verify exponentiation and fraction to decimal behave as expected."""
    assert exponentiate(2, 3) == 8
    # fraction_to_decimal returns a float; compare with approx
    assert fraction_to_decimal(1, 3) == pytest.approx(1 / 3)


def test_factorial():
    """Verify factorial for typical inputs and error for negative."""
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)


def test_gcd_lcm():
    """Verify gcd and lcm results for a few inputs."""
    assert gcd(48, 18) == 6
    assert gcd(-48, 18) == 6
    assert lcm(4, 5) == 20
    assert lcm(0, 5) == 0

