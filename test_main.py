"""Minimal pytest suite that tests the functions in main.py.
Contains 10 test functions. Each test function has at least 3 distinct cases
(normal, edge, and error where applicable) and brief comments.
"""
import pytest
import main


# 1) add - tests (normal, zero, negatives)
@pytest.mark.parametrize("inp,expected", [
    ((2, 3), 5),    # normal
    ((0, 0), 0),    # edge: zeros
    ((-1, 1), 0),   # negatives
])
def test_add(inp, expected):
    """Verify add((a,b)) returns a+b for several cases."""
    assert main.add(inp) == expected


# 2) divide - tests (normal, float, division by zero)
@pytest.mark.parametrize("inp,expected,raises", [
    ((6, 3), 2, None),
    ((1, 4), 0.25, None),
    ((5, 0), None, ZeroDivisionError),
])
def test_divide(inp, expected, raises):
    """Verify divide((a,b)). Includes division-by-zero error case."""
    if raises:
        with pytest.raises(raises):
            main.divide(inp)
    else:
        assert main.divide(inp) == pytest.approx(expected)


# 3) is_palindrome - tests (palindrome, non-palindrome, empty)
@pytest.mark.parametrize("s,expected", [
    ("Racecar", True),
    ("hello", False),
    ("", True),
])
def test_is_palindrome(s, expected):
    """Check simple palindrome behavior (lowercase comparison)."""
    assert main.is_palindrome(s) == expected


# 4) factorial - tests (positive, zero, negative error)
@pytest.mark.parametrize("n,expected,raises", [
    (5, 120, None),
    (0, 1, None),
    (-1, None, ValueError),
])
def test_factorial(n, expected, raises):
    """Factorial normal, zero, and negative error case."""
    if raises:
        with pytest.raises(raises):
            main.factorial(n)
    else:
        assert main.factorial(n) == expected


# 5) fibonacci - tests (base cases, normal, negative error)
@pytest.mark.parametrize("n,expected,raises", [
    (0, 0, None),
    (1, 1, None),
    (7, 13, None),
    (-2, None, ValueError),
])
def test_fibonacci(n, expected, raises):
    """Fibonacci base cases, a normal value, and error for negative."""
    if raises:
        with pytest.raises(raises):
            main.fibonacci(n)
    else:
        assert main.fibonacci(n) == expected


# 6) sort_items - tests (normal, empty, duplicates)
@pytest.mark.parametrize("items,expected", [
    ([3, 1, 2], [1, 2, 3]),
    ([], []),
    ([2, 1, 2], [1, 2, 2]),
])
def test_sort_items(items, expected):
    """Sorting behavior including empty list and duplicates."""
    assert main.sort_items(items) == expected


# 7) merge_dicts - tests (override, empty left, both empty)
@pytest.mark.parametrize("inp,expected", [
    (({'x': 1}, {'x': 2}), {'x': 2}),
    (({}, {'a': 5}), {'a': 5}),
    (({}, {}), {}),
])
def test_merge_dicts(inp, expected):
    """Merge two dicts given as one input tuple (a,b)."""
    assert main.merge_dicts(inp) == expected


# 8) parse_date - tests (valid, another valid, invalid format)
@pytest.mark.parametrize("s,expected,raises", [
    ("2020-01-01", (2020, 1, 1), None),
    ("1999-12-31", (1999, 12, 31), None),
    ("not-a-date", None, ValueError),
])
def test_parse_date(s, expected, raises):
    """Parse simple YYYY-MM-DD to (year, month, day) tuple or raise ValueError."""
    if raises:
        with pytest.raises(raises):
            main.parse_date(s)
    else:
        assert main.parse_date(s) == expected


# 9) normalize_text - tests (whitespace/punctuation, already normalized, empty)
@pytest.mark.parametrize("s,expected", [
    ("  Hello ", "hello"),
    ("WORLD", "world"),
    ("", ""),
])
def test_normalize_text(s, expected):
    """Basic normalization: strip and lower."""
    assert main.normalize_text(s) == expected


# 10) calculate_stats - tests (normal, even-length median, empty error)
@pytest.mark.parametrize("numbers,exp_mean,exp_median,exp_mode,raises", [
    ([1, 2, 3], 2.0, 2, 2, None),
    ([1, 2, 3, 4], 2.5, 2.5, None, None),
    ([], None, None, None, ValueError),
])
def test_calculate_stats(numbers, exp_mean, exp_median, exp_mode, raises):
    """Mean/median/mode computation and error on empty list."""
    if raises:
        with pytest.raises(raises):
            main.calculate_stats(numbers)
    else:
        mean, median, mode = main.calculate_stats(numbers)
        assert mean == pytest.approx(exp_mean)
        assert median == exp_median
        assert mode == exp_mode
