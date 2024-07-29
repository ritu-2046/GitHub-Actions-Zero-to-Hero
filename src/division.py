# app.py
# This is a the Multiplication functionality

def divide(a, b):
    return a / b

def test_divide():
    assert divide(6, 2) == 3
    assert divide(1, -1) == -1
    assert divide(-1, 0) == inf
