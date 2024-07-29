# app.py
# This is a the addition functionality

def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1, -1) == 2
    assert subtract(-1, -3) == 2
