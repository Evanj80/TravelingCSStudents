Nearest Neighbor Algorithm

Greedy algorithm that picks the best possible edge to use at each iteration.
The algorithm will not return to the root vertex until it visits all vertices.

Given a complete graph G(V,E).
Let P = { u } be the path found by the algorithm.

Initialize: Pick a vertex u ∈ V.
Iteration:
1. Pick a vertex v ∈ V that is nearest to P.V[0] (min uv).
2. Add v to P.V.
3. If P.V ≡  G.V, return to initial vertex.
4. Else, u=v and repeat the iteration.

Running Time: O(n²)

Notable changes:
Modified the original Graph.py to work with this algorithm.
As vertex and edge datas are read, convert them to numbers.
See diffGraphs.patch for more details.

Tests:
1. test1-edges.txt, test1-vertices.txt
= Cyclic graph with 2 vertices and 2 edges of same weight.
0 <-> 1

2. test2-edges.txt, test2-vertices.txt
= Acyclic graph with 3 vertices and 2 edges of same weight,
last vertex does not have an edge to other vertices.
0 -> 1 -> 2

3. test3-edges.txt, test3-vertices.txt
= Cyclic graph with 3 vertices and 3 edges of same weight.
0 -> 1 -> 2 -> 0 ...

4. test4-edges.txt, test4-vertices.txt
= Cyclic graph with 3 vertices and 6 edges of different weights.
0 -(1)-> 1 -(2)-> 2 -(1)-> 0
0 <-(2)- 1 <-(1)- 2 <-(2)- 0

5. test5-edges.txt, test5-vertices.txt
= Cyclic graph with 4 vertices and 6 edges of different weights,
vertices 0,1,2 are configured like in test4
vertex 3 is not connected to other vertices.
0 -(1)-> 1 -(2)-> 2 -(1)-> 0   3
0 <-(2)- 1 <-(1)- 2 <-(2)- 0

