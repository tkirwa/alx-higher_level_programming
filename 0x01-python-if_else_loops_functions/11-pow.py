#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    elif a < 0 and b % 2 == 0:
        a = abs(a)
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for i in range(b):
        result *= a
    return round(result, 4)
