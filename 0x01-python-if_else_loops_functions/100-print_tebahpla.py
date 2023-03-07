#!/usr/bin/python3

ascii_val = ord('z')
counter = 0

while ascii_val >= ord('A'):
    if counter % 2 == 0:
        print("{:c}".format(ascii_val), end="")
    else:
        print("{:c}".format(ascii_val).upper(), end="")
    ascii_val -= 1
    counter += 1
