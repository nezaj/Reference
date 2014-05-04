from nose.tools import eq_

from analysis import bisection

def test_bisection():
    arr = [1, 2, 3, 4, 5]

    # Finds 1 in position 0
    i = bisection(arr, 1)
    eq_(i, 0)

    # Finds 4 in position 3
    i = bisection(arr, 4)
    eq_(i, 3)

    # Cannot find index for 6
    i = bisection(arr, 6)
    eq_(i, None)

    arr = [-1, 200, 999]

    # Cannot find 0
    i = bisection(arr, 0)
    eq_(i, None)

    # Finds -1 in position 0
    i = bisection(arr, -1)
    eq_(i, 0)
