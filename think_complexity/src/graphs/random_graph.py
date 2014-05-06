"""
Random graph for exercise 2.4 from Think Complexity
"""

import itertools
import random
import math
import string
from collections import defaultdict

from graphs import Graph, Vertex, Edge, GraphError

class RandomGraph(Graph):

    def add_random_edges(self, p):
        " Adds edges at random with probability p between any two vertices of an empty graph "
        if p < 0 or p > 1:
            raise GraphError('Probability must be between 0 and 1')

        for vertex_pair in itertools.combinations(self.vertices(), 2):
            n = round(random.uniform(0, 1), 3)
            if p > n:
                self.add_edge(Edge(*vertex_pair))

def sharp_threshold():
    """
    Generates statistics for connectedness of a random Erdos-Renyi graph.
    Uses deltas between 0.0 and 1.0 in 0.1 increments
    """
    delta = 0.2
    vs = [Vertex(v) for v in string.ascii_letters]

    for d in xrange(0, 11, 1):
        delta = (d * 1.0) / 10

        res = defaultdict(lambda: 0)
        for n in xrange(1, len(vs)):
            random_vs = vs[:n]

            low_p = (1 - delta) * (math.log(n) / n)
            g = RandomGraph(random_vs, [])
            g.add_random_edges(low_p)
            if g.is_connected():
                res['low'] += 1


            high_p = (1 + delta) * (math.log(n) / n)
            g = RandomGraph(random_vs, [])
            g.add_random_edges(high_p)
            if g.is_connected():
                res['high'] += 1

        l_res = (res['low']  * 1.0) / len(vs)
        h_res = (res['high'] * 1.0) / len(vs)
        print "Delta {}: Low -- {}, High -- {}".format(delta, l_res, h_res)

if __name__ == '__main__':
    sharp_threshold()
