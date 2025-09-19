from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("OUTATIME") == False  
    assert is_valid("AAA222") == True

def test_invalid_start():
    assert is_valid("50CS") == False
    assert is_valid("1ABC") == False

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_zero_placement():
    assert is_valid("CS05") == False

def test_number_placement():
    assert is_valid("CS50P") == False
    assert is_valid("CS1234") == True
    assert is_valid("CS123P") == False

def test_alphanumeric():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False

def test_invalid_start():
    assert is_valid("12AB") == False
    assert is_valid("A2B3") == False
    assert is_valid("1A") == False
    assert is_valid("A1") == False

