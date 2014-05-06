import string
from nose.tools import eq_, assert_raises

from analysis import HashMap

class TestHashMap(object):

    def setUp(self):
        self.h = HashMap()
        lc = string.ascii_lowercase
        items = zip(lc, xrange(len(lc)))
        for k, v in items:
            self.h.add(k, v)

    def tearDown(self):
        pass

    def test_num(self):
        eq_(self.h.num, len(string.ascii_lowercase))

    def test_get(self):
        eq_(self.h.get('a'), 0)
        eq_(self.h.get('z'), 25)
        assert_raises(KeyError, self.h.get, 'aa')

    def test_iteritems(self):
        m = self.h.maps.iteritems()
