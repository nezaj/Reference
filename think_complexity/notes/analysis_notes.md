## Chapter 3: Analysis of Algorithms
### Exercise 3.1
```
1. What is the order of growth of n^3 + n^2? What about 1000000n^3 + n^2? What about n^3 + 1000000n^2?
```
In all three cases O(n) = n^3

```
2. What is the order of growth of (n^2 + n) · (n + 1)? Before you start multiplying, remember that you only need the leading term.
```
Once again, O(n) = n^3

```
3. If f is in O(g), for some unspecified function g, what can we say about a*f + b?
```
It is also in O(g)

```
4. If f1 and f2 are in O(g), what can we say about f1 + f2?
```
It is also in O(g)

```
5. If f1 is in O(g) and f2 is in O(h), what can we say about f1 + f2?
```
f1 + f2 is in max(O(g), O(h))

```
6. If f1 is in O(g) and f2 is O(h), what can we say about f1 ∗ f2?
```
f1 * f2 is in O(g) * O(h)

### Binary Trees
A **K-ary** tree is a **rooted** tree where each node has no more than *k* children.

A **binary tree** is a **tree data structure** in which each node has at most 2 children. A binary tree is a special case of a **K-ary** tree where *k* = 2.

A **binary search tree (BST)** is an ordered binary tree where each node has a comparable key (and an associated value) with the restriction that the key in any node is larger than all the keys in the node's left sub-tree and the key is smaller than all the keys in the node's right sub-tree. The common properties of BSTs are:

* The left sub-tree of a node contains only nodes with keys less than the node's key
* The right sub-tree of a node contains only nodes with keys larger than the node's key
* The left and right subtree each must also be a BST
* Each node can have up to two successor nodes
* There must be no duplicate nodes.
* A unique path exists from the root to every other node

A **self-balancing binary search tree** is any node-based BST that automatically keeps its height (maximal number of levels below the root) small in the face of arbitrary insertions and deletions.

These structures provide efficient implementations for mutable ordered lists and can be used for other abstract data structures.

Most operations on a BST takes time directly proportional to the height of the tree, so it is desirable to keep the height small. A binary tree with height *h* can contain at most *2^0 + 2^1 + ... + 2^h = 2^h+1 - 1* nodes. Thus, for a tree with *n* nodes and height *h*
```
n <= 2^(h + 1) - 1
=> h >= round_up(log(n + 1) - 1) >= round_down(log(n))
=> h >= round_down(log(n))
```
Thus the minimum height of a tree with *n* nodes is **log(n)**

However, the simplest algorithms for BST item insertion may result in trees
with height *n*. For example when the items are inserted in sorted key order, the tree degenerates into a linked list with *n* nodes. The difference in performance between the two situations may be enormous: for *n = 1,000,000* the minimum height is *round_down(log(1,000,000)) = 19*

Self-balancing binary trees solve this problem by performing transformations on the tree (such as tree rotations) at key times, in order to keep the heigh proportional to log(n). Although a certain overhead is incurred, it may be justified in the long run by ensuring fast execution of later operations.

A **red-black tree** is type of of self-balancing BST.
