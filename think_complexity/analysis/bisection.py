
def bisection(l, t, shift=0):
    """
    Uses binary search to find index of target in a list. Assumes list is sorted

    Algorithm:
    If the list is empty than the target cannot be located. Return None.

    For a non-empty list, check whether the middle element is the target.
    If it is, return the middle index plus all previously discarded elements.
    If it isn't and the middle index is 0 than the target does not exist.
    Return None.

    If the target is smaller than the middle element, search the left half of the
    list. If the target is larger than the middle element, search the right half
    of the list. When searching the right half, we must keep track of all the
    discarded elements to the left.
    """
    if l == []:
        return None

    mid = len(l) / 2
    if t == l[mid]:
        return shift + mid
    if mid == 0:
        return None

    if t < l[mid]:
        return bisection(l[:mid], t, shift)
    else:
        return bisection(l[mid:], t, shift + mid)
