"""
Graph code from Chapter 2 of Think Complexity
"""

class Graph(dict):
    """
    Implements an undirected graph as a dictionary of dictionaries.

    Graph is a dictionary that maps from a vertix V to an inner dictionary
    that maps from a vertix W to an Edge that connect V and W.

    Suppose g is a graph, g[v][w] maps to an Edge if there is one or raises
    a KeyError if there is not one.

    Adding a vertex V to a Graph creates a new entry in the outer dictionary,
    Adding an edge E to a Graph creates two near entries in the inner dictionary
    which both point to the same Edge.
    """

    def __init__(self, vs=[], es=[]):
        """
        Creates a new graph.
        vs: a list of vertices
        es: a ist of edges
        """
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_edge(self, e):
        """
        Adds edge to graph by adding entry for both directions.
        If there already exists an edge between the vertices it is
        replaced by this new one.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def add_vertex(self, v):
        " Adds vertix to graph "
        self[v] = {}

class Vertex(object):
    " A Vertex is a node in a graph. "
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return "Vertex('{}')".format(self.label)

    __str__ = __repr__

class Edge(tuple):
    " An Edge is a tuple of two vertices. "
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1,e2))

    def __repr__(self):
        return 'Edge({}, {})'.format(repr(self[0]), repr(self[1]))

    __str__ = __repr__
