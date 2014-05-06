from nose.tools import eq_

from graphs import alphanum_generator

def test_alphanum_generator():
    # First 10 elements is a list a1, a2, ... a9
    g = alphanum_generator()
    exp = [('a' + str(i)) for i in xrange(1, 10)]
    act = []
    for i in xrange(1, 10):
        act.append(g.next())

    eq_(act, exp)

    # Next 10 elements is a list b1, b2, ... b9
    exp = [('b' + str(i)) for i in xrange(1, 10)]
    act = []
    for i in xrange(1, 10):
        act.append(g.next())

    eq_(act, exp)

    # 234th element is 'z9'
    g = alphanum_generator()
    for i in xrange(1, 234):
        g.next()

    eq_(g.next(), 'z9')

    # 235th element is 'a1'
    eq_(g.next(), 'a1')
