from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_0():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected


def test_fibonacci_1():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected


def test_fibonacci_3():
    expected = 2
    actual = fibonacci(3)
    assert actual == expected


def test_lucas_0():
    expected = 2
    actual = lucas(0)
    assert actual == expected


def test_lucas_1():
    expected = 1
    actual = lucas(1)
    assert actual == expected


def test_lucas_2():
    expected = 3
    actual = lucas(2)
    assert actual == expected


def test_lucas_3():
    expected = 4
    actual = lucas(3)
    assert actual == expected


def test_sum_series_with_no_optional():
    expected = 21
    actual = sum_series(8)
    assert actual == expected


def test_sum_series_with_2_and_1_optional():
    expected = 11
    actual = sum_series(5, 2, 1)
    assert actual == expected


def test_sum_series_other():
    expected = 521
    actual = sum_series(10, 4, 7)
    assert actual == expected


def test_fibonacci_neg_num():
    expected = "You pass negative number"
    actual = fibonacci(-1)
    assert actual == expected


def test_lucas_neg_num():
    expected = "You pass negative number"
    actual = lucas(-1)
    assert actual == expected


def test_sum_series_neg_num():
    expected = "You pass negative number"
    actual = sum_series(-1)
    assert actual == expected
