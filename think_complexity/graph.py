"""
Graph code from Chapter 2 of Think Complexity
"""

import itertools
import math

from util import rotate_list, is_even, is_odd

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

    def add_all_edges(self):
        " Makes a complete graph by adding edges to it "
        for vertex_pair in itertools.combinations(self.vertices(), 2):
            self.add_edge(Edge(*vertex_pair))

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
        " Adds vertex to graph "
        self[v] = {}

    def edges(self):
        " Returns a sorted list of edges in the graph "
        edges = set()
        for v in self.values():
            edges.update(v.values())

        return sorted(list(edges))

    def get_edge(self, v, w):
        " Takes two vertices and returns the edge between them if it exists "
        try:
            return self[v][w]
        except KeyError:
            return None

    def num_edges(self):
        " Convienence method for number of edges in graph"
        return len(self.edges())

    def num_vertices(self):
        " Convienence method for number of vertices in graph"
        return len(self.vertices())

    def out_edges(self, v):
        " Returns a sorted list of edges connected to the given vertex "
        return sorted(self[v].values())

    def out_vertices(self, v):
        " Returns a list of of vertices with an edge to the given vertex "
        return sorted(self[v].keys())

    def remove_edge(self, e):
        " Removes edge from graph by removing entries for both directions "
        v, w = e
        self[v][w] = None
        self[w][v] = None

    def vertices(self):
        " Returns a sorted list of vertices in the graph. "
        return sorted(self.keys())

class Vertex(object):
    " A node in a graph. "
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return "Vertex('{}')".format(self.label)

    def __lt__(self, other):
        " Vertices are sorted lexicographically by label "
        return self.label < other.label

    __str__ = __repr__

class Edge(tuple):
    " A tuple of two vertices. "
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1,e2))

    def __repr__(self):
        return 'Edge({}, {})'.format(repr(self[0]), repr(self[1]))

    def __lt__(self, other):
        " Edges are sorted lexicographically by vertex "
        if self[0] == other[0]:
            return self[1] < other[1]
        else:
            return self[0] < other[0]

    __str__ = __repr__

def mock_graph():
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    g = Graph([v, w], [e])
    return g
