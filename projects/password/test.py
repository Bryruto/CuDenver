from hash import fix,my_hash

def test_fix():

    assert fix(my_hash("AbC")) == "AbC"
    assert fix(my_hash("HelloWorld")) == "HelloWorld"
    assert fix(my_hash("abcXYZ")) == "abcXYZ"
    assert fix(my_hash("zzzz")) == "zzzz"
