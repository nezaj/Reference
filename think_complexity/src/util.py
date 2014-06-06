"""
Useful helper functions
"""

import os
from contextlib import contextmanager

def rotate_list(l, n):
    " Rotate a list n units to the right "
    return l[n:] + l[:n]

def is_even(n):
    " Returns whether a number is even "
    return (n % 2) == 0

def is_odd(n):
    " Returns whether a number is odd "
    return not is_even(n)

def etime():
    """
    Returns the sum of user and system time used by this process
    """
    user, sys, _, _, _ = os.times()
    return user + sys

@contextmanager
def timer():
    """
    Prints elapsed time of work. Useful for timing functions.
    """
    start = etime()
    try:
        yield
    finally:
        end = etime()

    elapsed = end - start
    print "Time elapsed: {}".format(elapsed)
