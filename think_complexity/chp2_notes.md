## Chapter 2
### Exercise 2.1
```
1. What is a simple graph? In the rest of this section, we will be assuming that all graphs are simple graphs. This is a common assumption for many graph algorithms—so common it is often unstated.
```
A simple a graph is an undirected graph with no loops. There exists no more than one edge between any two different vertices. Each edge represents a distinct pair of vertices. The edges of a simple graph are a set. In a simple graph with N vertices each vertex has a degree less than N.

```
2. What is a regular graph? What is a complete graph? Prove that a complete graph is regular.
```
A regular graph is graph where each vertex has the same degree. A complete graph is a graph where there exists an edge between any two vertices of the graph.
> Proof:
    Suppose `G` is a complete graph that is not regular.
    => There exists a vertex `x` with degree `M` and a vertex `y` with degree `N` != `M`.
    Contradiction! Since `G` is a complete graph there exists an edge between any two vertices of a graph
    => All vertices have degree `n-1`.
    => Thus G must be regular.

```
3. What is a path? What is a cycle?
```
A path is a set of edges which start at a vertex `A` and ends at a vertex `B`. A cycle is a path that starts and ends at the same vertex.

```
4. What is a forest? What is a tree? Note: a graph is connected if there is a path from every node to every other node.
```
A forest is a disjoint union of trees. A tree is a connected graph where there exists only one path for any pair of vertices, or a connected graph without simple cycles.
