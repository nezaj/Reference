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
