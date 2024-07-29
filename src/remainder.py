# app.py
# This is a the Remainder functionality

def remainder(a, b):
    return a % b

def test_remainder():
    assert remainder(6, 2) == 0
    assert remainder(10, -4) == -2
    assert remainder(18, 5) == 3
