#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list: A list of integers.

    Returns:
        A new list with True or False, depending on whether the integer at the same
        position in the original list is a multiple of 2. The new list should have
        the same size as the original list.
    """
    return [True if i % 2 == 0 else False for i in my_list]
