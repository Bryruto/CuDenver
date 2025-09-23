from twttr import shorten

def test_correct():
    assert shorten("brycen") == 'brycn'

def test_puctuation():
    assert shorten("bry.bry?") == 'bry.bry?'

def test_numbers():
    assert shorten("111") == '111'

def test_cap():
    assert shorten("AEIOU") == ''
