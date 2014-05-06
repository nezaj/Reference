
class LinearMap(object):
    " Simple map implementation. Defines add and get operations with constant and linear time respectively "
    def __init__(self):
        self.items = []

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        for key, value in self.items:
            if key == k:
                return value
        raise KeyError

class BetterMap(object):
    " Improvement over LinearMap. Uses multiple LinearMaps to store keys to reduce linear lookup time of get"
    def __init__(self, n=100):
        self.maps = []
        for i in xrange(n):
            self.maps.append(LinearMap())

    def get_map(self, k):
        i = hash(k) % len(self.maps)
        return self.maps[i]

    def add(self, k, v):
        m = self.get_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.get_map(k)
        return m.get(k)

    def __len__(self):
        return len(self.maps)

    def iteritems(self):
        for m in self.maps:
            yield m

class HashMap(object):
    " Improvement over BetterMap. Average cost of get and add is expected to be closer to constant time "
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def add(self, k, v):
        if self.num == len(self.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    def get(self, k):
        return self.maps.get(k)

    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.iteritems():
            for k, v in m.items:
                new_maps.add(k, v)

        self.maps = new_maps
