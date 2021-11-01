from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fib_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_2():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 3
    assert actual == expected

def test_lucas_5():
    actual = lucas(5)
    expected = 8
    assert actual == expected

def sum_series_negative():
    actual = sum_series(-1)
    expected = "Can't perform on negative numbers"
    assert actual == expected

def sum_series_1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def sum_series_5():
    actual = sum_series(5)
    expected = 5
    assert actual == expected   

def sum_series_10():
    actual = sum_series(10)
    expected = 55
    assert actual == expected 

def sum_series_10():
    actual = sum_series(10, 2, 3)
    expected = 233
    assert actual == expected 