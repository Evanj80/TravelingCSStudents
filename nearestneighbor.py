#
# nearestneighbor.py
# 
# Implementation of nearest neighbor algorithm.
# 
# (c) Alvin Nguyen
#
from Graph import Graph
import sys
import time
import tracemalloc

# Sum edges in path by iterating each edge per vertex.
#
def sum_edges(g):
    sum=0.0
    for edgelist in g.vertex_weights.values():
        for edge in edgelist:
            for w in edge.values():
                sum += w
    return sum;

# Nearest Neighbor algorithm 
# @param g Graph to search
# @param start_u Original vertex when starting search
# @param u Current vertex during search
# @param p Path (Graph)
#
def nearest_neighbor(g, start_u, u, p):
    # Summarize sum of edges in p
    psum_edges = sum_edges(p)

    # Init
    # min_edge the maximum float in the system,
    # vertex v = u,
    # weight w = 0.0
    min_edge = max(sys.float_info)
    v = u
    w = 0.0

    # Main Part of the algorithm: Find the lowest weighted edge.
    # For each adjacent edge from u in g:
    # 1. Find a vertex ev ∉ p.
    # 2. Test if psum_edges + weight ew < min_edge is true.
    # 3. Update min_edge = psum_edges + weight ew.
    # 4. Set v = ev.
    # 5. Set w = ew.
    # 
    for edge in g.vertex_weights[u]:
        for ev,ew in edge.items():
            if (ev not in p.vertex_weights):
                if (psum_edges + ew < min_edge):
                    min_edge = psum_edges + ew
                    v = ev
                    w = ew

    # WIP
    # If v == u, then need to reroute nearest neighbor.
    # May not be used in most cases.
    # Initialize: Pick a vertex bv ∈ g and bv ∉ p.
    # 1. Start breadth-first search from bu and bv.
    # 2. If there exists one vertex x, such that x ∈ V AND x ∈ P,
    #    OR the path from u to x to v is the shortest path,
    #    then add a path from u to v that includes x.
    # 3. Else, repeat the iteration.
    #if v == u:
    #    bp = Graph()
    #    bp.addVertex(v)
    #    bu = Graph()
    #    bu.addVertex(v)
    #    bv = Graph()
    #    vb = -1
    #    for vm in g.vertex_weights:
    #        if (vm not in p.vertex_weights) and (!nv):
    #            bv.addVertex(vm)
    #            vb = vm
    #    x = -1
    #    xfound = False
    #    while !xfound:
    #        # BFS from bu and bv
    #        for edge in g.vertex_weights[bu]:
    #            for ev,ew in edge.items():
    #                bu.addEdge(v,ev,ew)
    #        for edge in g.vertex_weights[bv]:
    #            for ev,ew in edge.items():
    #                bv.addEdge(vb,ev,ew)
    #        # If there exist a vertex shared by bu and bv, set x to bx
    #        for bx in bu.vertex_weights:
    #            if (bx is in bv.vertex_weights):
    #                x = bx
    #                xw = bu.vertex_weights[x][x]
    #                xfound = True
        

    # Add v to p, if it is new.
    if (v not in p.vertex_weights):
        p.addVertex(v)
        p.addEdge(u,v,w)

    if (g.number_of_vertices == p.number_of_vertices):
        # If g.V == p.V is true, find an edge from v to start_u.
        for edge in g.vertex_weights[v]:
            for ev,ew in edge.items():
                if (ev == start_u):
                    p.addEdge(v,ev,ew)
        return p
    else:
        # If g.V == p.V is False, run nearest_neighbor starting from v.
        nearest_neighbor(g, start_u, v, p)

# Testing Section
# nearestneighbor usage
if (len(sys.argv) >= 4):
    vfile = sys.argv[1]
    efile = sys.argv[2]
    root = int(sys.argv[3])
else:
    print("USE: python nextneighbor.py vfile efile root",
        "\nvfile = vertices file"
        "\nefile = edges file"
        "\nroot = vertex to start nearest neighbor algorithm"
        "\nExample: python nextneighbors.py test1-vertices.txt test1-edges.txt 0"
    ) 
    exit()

# Graph created from passed-in arguments.
a = Graph(vfile,efile)
print("Graph a:", len(a.vertex_weights), "vertices")
a.adjlist()

# Empty graph representing the path used in nearest neighbors.
b = Graph()
b.addVertex(root)
print("Graph b: (before nearest_neighbor)", len(b.vertex_weights), "vertices")
b.adjlist()

# 1. Start measuring memory usage with tracemalloc.
# 2. Start measuring the running time of nearest neighbor with time.monotonic().
# 3. Run nearest neighbor.
# 4. Get the current and peak memory usage.
# 5. Stop measuring the running time.
# 6. Stop measuring memory usage.
tracemalloc.start()
start = time.monotonic()
nearest_neighbor(a, root, root, b)
current, peak = tracemalloc.get_traced_memory()
stop = time.monotonic()
tracemalloc.stop()

# Found path after running nearest neighbor
print("Graph b: (after nearest_neighbor)", len(b.vertex_weights), "vertices")
b.adjlist()

# Print duration to complete program, cost of path, and memory usage
print("Time %f" %(float(stop-start)))
print("Cost %f" %sum_edges(b))
print("Memory: %f MB (current), %f MB (max)" %(current/10**6, peak/10**6))

