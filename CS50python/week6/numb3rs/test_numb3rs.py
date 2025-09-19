from numb3rs import validate

def test_false():
    assert validate(r"300.33.33.33") == False
    assert validate(r"30.330.33.33") == False
    assert validate(r"30.33.330.33") == False
    assert validate(r"30.33.33.330") == False

def test_vaid():
    assert validate(r"233.22.22.22") == True
    assert validate(r"233.22.22") == False
    assert validate(r"233.22") == False
    assert validate(r"233") == False

