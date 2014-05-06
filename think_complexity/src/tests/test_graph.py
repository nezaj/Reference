from nose.tools import eq_, assert_raises

from graphs import Graph, Vertex, Edge, GraphError

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

    def test_add_all_edges(self):
        # Adds an edge to edge-less graph
        v, w, e = self.v, self.w, self.e
        g = Graph([v, w], [])
        g.add_all_edges()
        eq_(g.edges(), [e])

        # Adds edges between all pairs of vertices in edge-less graph
        x = Vertex('x')
        e2 = Edge(v, x)
        e3 = Edge(w, x)
        g = Graph([v, w, x], [])
        g.add_all_edges()
        eq_(g.edges(), [e, e2, e3])

    def test_add_regular_edges(self):
        # Adds an edge to edge-less graph
        v, w, e = self.v, self.w, self.e
        g = Graph([v, w], [])
        g.add_regular_edges(1)
        eq_(g.edges(), [e])

        # Can make a regular graph of three vertices and degree 2
        x = Vertex('x')
        e2 = Edge(v, x)
        e3 = Edge(w, x)
        g = Graph([v, w, x], [])
        g.add_regular_edges(2)
        eq_(g.edges(), [e, e2, e3])

        # Cannot make a regular graph of three vertices and degree 1
        g = Graph([v, w, x], [])
        assert_raises(GraphError, g.add_regular_edges, 1)

        # Cannot make a regular graph of three vertices and degree 3
        g = Graph([v, w, x], [])
        assert_raises(GraphError, g.add_regular_edges, 3)

        # Can make a regular graph of five vertices and even degree
        y = Vertex('y')
        z = Vertex('z')
        g = Graph([v, w, x, y, z], [])
        g.add_regular_edges(2)
        eq_(g.num_edges(), 5)

        # Can make a regular graph of 4 vertices and odd degree
        g = Graph([v, w, x, y], [])
        g.add_regular_edges(3)
        eq_(g.num_edges(), 6)

        # Cannot make a regular graph of five vertices and degree 3
        g = Graph([v, w, x, y, z], [])
        assert_raises(GraphError, g.add_regular_edges, 3)

    def test_is_connected(self):
        # Returns False for an empty graph
        v, w, e = self.v, self.w, self.e
        g = Graph([v, w], [])
        eq_(g.is_connected(), False)

        # Returns True for a complete graph
        g.add_all_edges()
        eq_(g.is_connected(), True)

        # Returns False when a new vertex is added
        x = Vertex('x')
        g.add_vertex(x)
        eq_(g.is_connected(), False)

        # Returns True when edge is added to connect it
        e2 = Edge(w, x)
        g.add_edge(e2)
        eq_(g.is_connected(), True)
