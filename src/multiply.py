# app.py
# This is a the Multiplication functionality

def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1, -1) == -1
    assert multiply(-1, -2) == 2
    assert multiply(1, 0) == 0
