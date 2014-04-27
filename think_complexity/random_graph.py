"""
Random graph for exercise 2.4 from Think Complexity
"""

import itertools
import random

from graph import Graph, Edge, GraphError

class RandomGraph(Graph):

    def add_random_edges(self, p):
        " Adds edges at random with probability p between any two vertices of an empty graph "
        if p < 0 or p > 1:
            raise GraphError('Probability must be between 0 and 1')

        for vertex_pair in itertools.combinations(self.vertices(), 2):
            n = round(random.uniform(0, 1), 3)
            if p > n:
                self.add_edge(Edge(*vertex_pair))
