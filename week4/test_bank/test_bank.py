
from bank import value


def test_case():
    assert value("H") == 20

def test_anyother():
    assert value("BRYCEN my name is") == 100

def test_hello_phrase():
    assert value("hello, friend") == 0
