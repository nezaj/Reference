"""
Useful helper functions
"""

def rotate_list(l, n):
    " Rotate a list n units to the right "
    return l[n:] + l[:n]

def is_even(n):
    " Returns whether a number is even "
    return (n % 2) == 0

def is_odd(n):
    " Returns whether a number is odd "
    return not is_even(n)
