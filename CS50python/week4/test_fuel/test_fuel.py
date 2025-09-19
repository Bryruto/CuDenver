import pytest
from fuel import convert, gauge

# ----- Tests for convert -----
def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3//4")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/2")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_greater_than_one():
    with pytest.raises(ValueError):
        convert("5/4")

# ----- Tests for gauge -----
def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
