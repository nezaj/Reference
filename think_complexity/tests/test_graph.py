from nose.tools import eq_

from graph import Graph, Vertex, Edge


class TestGraph(object):

    def setUp(self):
        self.v = Vertex('v')
        self.w = Vertex('w')
        self.e = Edge(self.v, self.w)
        self.g = Graph([self.v, self.w], [self.e])

    def tearDown(self):
        pass

    def test_get_edge(self):
        v, w, e, g = self.v, self.w, self.e, self.g

        # Edge is returned when edge exists
        eq_(g.get_edge(v, w), e)

        # None is returned when edge does not exist
        x = Vertex('x')
        eq_(g.get_edge(v, x), None)
        eq_(g.get_edge(v, v), None)

    def test_remove_edge(self):
        v, w, e, g = self.v, self.w, self.e, self.g

        # Edge is returned when edge exists
        eq_(g.get_edge(v, w), e)

        # Edge does not exist after it has been removed
        g.remove_edge(e)
        eq_(g.get_edge(v, w), None)

    def test_vertices(self):
        # Returns a list of vertices in the graph
        v, w, e, g = self.v, self.w, self.e, self.g
        eq_(g.vertices(), [v, w])

        # Returns an updated
        x = Vertex('x')
        g.add_vertex(x)
        eq_(g.vertices(), [v, w, x])

    def test_edges(self):
        # Returns a list of edges in the graph
        v, w, e, g = self.v, self.w, self.e, self.g
        eq_(g.edges(), [e])

        # Add a new vertex and edge
        x = Vertex('x')
        g.add_vertex(x)
        e2 = Edge(v, x)
        g.add_edge(e2)

        # New edge is included
        eq_(g.edges(), [e, e2])

    def test_out_edges(self):
        # Returns a list of edges connected to a vertex
        v, w, e, g = self.v, self.w, self.e, self.g
        eq_(g.out_edges(v), [e])

        # Add a new vertex and edge
        x = Vertex('x')
        g.add_vertex(x)
        e2 = Edge(v, x)
        g.add_edge(e2)

        # New edge is included only for v and x
        eq_(g.out_edges(v), [e, e2])
        eq_(g.out_edges(w), [e])
        eq_(g.out_edges(x), [e2])

    def test_out_vertices(self):
        # Returns a list of adjacent vertices in the graph
        v, w, e, g = self.v, self.w, self.e, self.g
        eq_(g.out_vertices(v), [w])

        # Add a new vertex and edge
        x = Vertex('x')
        g.add_vertex(x)
        e2 = Edge(v, x)
        g.add_edge(e2)

        # New vertex is included
        eq_(g.out_vertices(v), [w, x])
