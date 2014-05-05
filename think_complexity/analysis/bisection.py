"""
Binary search thanks to bisect module
https://docs.python.org/2/library/bisect.html#searching-sorted-lists
"""

import bisect

def bisection(l, t):
    """
    Finds index of target in a list. Returns None if not found.
    Note: Assumes list is already sorted
    """
    i = bisect.bisect_left(l, t)
    if i != len(l) and l[i] == t:
        return i

    return None
