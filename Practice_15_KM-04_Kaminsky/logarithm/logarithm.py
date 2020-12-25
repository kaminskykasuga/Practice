from math import log as l

def log(a, b):
    try:
        assert (a > 0) and (a != 1) and (b > 0)
        return l(b, a)
    except:
        print('Error!')

def ln(b):
    try:
        assert b > 0
        return l(b)
    except:
        print('Error!')

def lg(b):
    try:
        assert b > 0
        return l(b, 10)
    except:
        print('Error!')