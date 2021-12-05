================================================================================
readme.txt
Team 2 TSP
Alvin Nguyen

Alvin's Working Directory for the Travelling Salemans Problem
================================================================================
Nearest Neighbor Algorithm

Heuristic with Greedy criterion
that picks the best possible edge to use at each iteration.
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
Space Complexity: O(V+E)
================================================================================
Descriptions for Programs

* Graph.py:
Graph class for building a network.

* nearestneighbor.py:
Implementation of nearest neighbor algorithm.

* net.py:
Python script to graph a network
using vertices and edges from some datasets

* bulgaria10run.sh:
Run nearest neighbor for bulgaria dataset with 10 villages.

* testcases.sh:
Run nearest neighbor starting at r with some test cases.

================================================================================
Descriptions for Directories

* b10fin:
Results from running nearest neighbors on the Bulgaria dataset of 10 villages.
These results were posted on the slides and report.

* b10out:
Working directory for running nearest neighbors
on the Bulgaria dataset of 10 villagers.
Saves the latest results from bulgaria10run.sh

* bulgaria:
Dataset of villages in Bulgaria retrieved from
G. C. Crisan, 2017, "Bulgaria TSP instance with GPS coordinates and GEO norm",
https://doi.org/10.7910/DVN/QCHUMD

bulgaria10-edges.tsp - 98 edges with weights for 10 villages
bulgaria10.tsp - vertices for 10 villages
bulgaria20-edges.tsp - 398 edges with weights for 20 villages
bulgaria20.tsp - vertices for 20 villages
bulgaria-full-edges.tsp - 3818114 edges with weights for 1954 villages
bulgaria-full.tsp - vertices for 1954 villages

bulgaria-full-edges.tsp and bulgaria-full.tsp are the complete dataset.

* nets:
Images produced from net.py

* sfroad:
Dataset of Road Networks in San Francisco, CA retrieved from
https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm

Original Creator:
T. Brinkoff, 2002, "A Framework for Generating Network-Based Moving Objects."
GeoInformatica, vol. 6, pp. 153–180, DOI:
https://doi.org/10.1023/A:1015231126594

* testcases:
Test cases for testing out the Graph and nearest neighbor algorithm.
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

================================================================================
Directory Tree

nearestneighbor
├── b10fin
│   ├── result-bulgaria10-01.txt
│   ├── result-bulgaria10-02.txt
│   ├── result-bulgaria10-03.txt
│   ├── result-bulgaria10-04.txt
│   ├── result-bulgaria10-05.txt
│   ├── result-bulgaria10-06.txt
│   ├── result-bulgaria10-07.txt
│   ├── result-bulgaria10-08.txt
│   ├── result-bulgaria10-09.txt
│   ├── result-bulgaria10-10.txt
│   └── results-bulgaria10.txt
├── b10out
│   ├── result-bulgaria10-01.txt
│   ├── result-bulgaria10-02.txt
│   ├── result-bulgaria10-03.txt
│   ├── result-bulgaria10-04.txt
│   ├── result-bulgaria10-05.txt
│   ├── result-bulgaria10-06.txt
│   ├── result-bulgaria10-07.txt
│   ├── result-bulgaria10-08.txt
│   ├── result-bulgaria10-09.txt
│   ├── result-bulgaria10-10.txt
│   └── results-bulgaria10.txt
├── bulgaria
│   ├── bulgaria10-edges.tsp
│   ├── bulgaria10.tsp
│   ├── bulgaria20-edges.tsp
│   ├── bulgaria20.tsp
│   ├── bulgaria-full-edges.tsp
│   └── bulgaria-full.tsp
├── bulgaria10run.sh
├── Graph.py
├── nearestneighbor.py
├── net.py
├── nets
│   ├── bulgaria-full.png
│   ├── path-nn1.png
│   ├── path-nn1.tsp
│   ├── path-nn2.png
│   ├── path-nn2.tsp
│   ├── path-nn3.png
│   └── path-nn3.tsp
├── readme.txt
├── sfroad
│   ├── edge_weights.txt
│   └── Nodes.txt
├── testcases
│   ├── test1-edges.txt
│   ├── test1-vertices.txt
│   ├── test2-edges.txt
│   ├── test2-vertices.txt
│   ├── test3-edges.txt
│   ├── test3-vertices.txt
│   ├── test4-edges.txt
│   ├── test4-vertices.txt
│   ├── test5-edges.txt
│   └── test5-vertices.txt
└── testcases.sh

================================================================================
