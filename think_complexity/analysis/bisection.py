
def bisection(l, t, shift=0):
    """
    Uses binary search to find index of target in a list.
    Note: Assumes list is already sorted
    """
    lo = 0
    hi = len(l)

    while lo < hi:
        mid = (lo + hi) / 2
        if t == l[mid]:
            return mid
        elif t < l[mid]:
            hi = mid
        else:
            lo = mid + 1

    return None
