# app.py
# This is a the addition functionality

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(0, -10) == -10
