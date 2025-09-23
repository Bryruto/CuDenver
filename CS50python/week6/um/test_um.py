from um import count

def test_uminword():
    assert count("um, um um. yummy") == 3
    assert count("yummy") == 0
    assert count("yes this is UM") == 1
    assert count("yummy yum tum") == 0

def test_count():
    assert count("yum um um. um,") == 3
    assert count("um y up ut") == 1
    assert count("y up ut um") == 1

