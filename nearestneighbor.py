from Graph import Graph
import sys

# print graph as an adjacency list
def adjlist(g):
    for u, edgelist in g.vertex_weights.items():
        children="->"
        for edge in edgelist:
            for v,w in edge.items():
                children += " %d, %f ->" % (v, w)
        print("%s %s" % (u, children))
    print()

# sum edges in path
def sum_edges(g):
    sum=0.0
    for edgelist in g.vertex_weights.values():
        for edge in edgelist:
            for w in edge.values():
                sum += w
    return sum;

# Nearest Neighbor algorithm implementation (W. I. P.)
def nearest_neighbor(g, start_u, u, p):
    psum_edges = sum_edges(p)
    min_edge = max(sys.float_info)
    v = u
    w = 0.0
    for edge in g.vertex_weights[u]:
        for ev,ew in edge.items():
            if (ev not in p.vertex_weights):
                if (psum_edges + ew < min_edge):
                    min_edge = psum_edges + ew
                    v = ev
                    w = ew

    if (v not in p.vertex_weights):
        p.addVertex(v)
        p.addEdge(u,v,w)

    if (g.number_of_vertices == p.number_of_vertices):
        for edge in g.vertex_weights[v]:
            for ev,ew in edge.items():
                if (ev == start_u):
                    p.addEdge(v,ev,ew)
        return p
    else:
        nearest_neighbor(g, start_u, v, p)

# Testing Section
if (len(sys.argv) >= 4):
    vfile = sys.argv[1]
    efile = sys.argv[2]
    root = int(sys.argv[3])
else:
    print("USE: python nextneighbors.py vfile efile root",
        "\nvfile = vertices file"
        "\nefile = edges file"
        "\nroot = vertex to start nearest neighbor algorithm"
        "\nExample: python nextneighbors.py test1-vertices.txt test1-edges.txt 0"
    ) 
    exit()

a = Graph(vfile,efile)
a.fixInput()
print("Graph a:", len(a.vertex_weights), "vertices")
adjlist(a)

b = Graph()
b.addVertex(root)
print("Graph b: (before nearest_neighbors)", len(b.vertex_weights), "vertices")
adjlist(b)

nearest_neighbor(a, root, root, b)

print("Graph b: (after nearest_neighbors)", len(b.vertex_weights), "vertices")
adjlist(b)
