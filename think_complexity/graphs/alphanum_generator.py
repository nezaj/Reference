import string

def alphanum_generator():
    """
    Yields an infinite sequence of alpha-numeric identifiers starting
    with a1 through z1, a2 through z2, up to a9 through z9 before wrapping
    around once more.
    """
    while True:
        for c in string.lowercase:
            for i in xrange(1, 10):
                yield c + str(i)
