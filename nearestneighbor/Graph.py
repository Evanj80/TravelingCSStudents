# 
# Graph.py
# 
# Graph class for building a network.
# 
# (c) Alvin Nguyen
# (c) Evan Chopra (original design)
# 
from collections import defaultdict

class Graph:
    # Filenames for list of vertices/edges.
    verticesfile = ""
    edgesfile = ""

    # Graph G(V, E) = { u ∈ V, [ { v ∈ V, w } ] ∈ E }
    vertex_weights = defaultdict(lambda : [])
    number_of_vertices = 0

    # Initialize a graph with a given vertices file and edges file.
    # If no vertices or edges files were used, then create an empty graph.
    # @param vf verticesfile
    # @param ef edgesfile
    #
    def __init__(self, vf="", ef=""):
        self.verticesfile = vf
        self.edgesfile = ef
        self.vertex_weights = {}
        self.number_of_vertices = 0
        if (len(self.verticesfile) > 0 and len(self.edgesfile) > 0):
            self.readInVertices()
            self.readInEdges()
    
    # Add a vertex to the Graph.
    # @param u vertex
    #
    def addVertex(self,u):
        if u in self.vertex_weights:
            return -1
        else:
            self.vertex_weights[u] = []
            self.number_of_vertices += 1

    # Add an edge between u and v with a weight w.
    # @param u source vertex
    # @param v destination vertex
    # @param w weight
    #
    def addEdge(self,u,v,w):
        self.vertex_weights[u].append({v:w})
            
    # Print data structure of graph as dictionary with list of dictionaries.
    # For debugging purposes.
    #
    def print_graph(self):
        for i in self.vertex_weights.items():
            print(i)
            
    # Read vertices from verticesfile and add them to the graph.
    #
    def readInVertices(self):
        vertices = [x.replace("\n","").split(' ')[0]
                for x in open(self.verticesfile).readlines()]
        for i in vertices:
            self.addVertex(int(i))

    # Read edges and weights from edgesfile and add them to the graph.
    #
    def readInEdges(self):
        with open(self.edgesfile) as file:
            for line in file:
                line = line.split(" ")
                starting_vertex = int(line[1])
                end_vertex = int(line[2])
                weight_between = float(line[3])
                self.addEdge(starting_vertex,end_vertex,weight_between)

    # Print a graph as an adjacency list.
    # Ex:
    # 0 -> 1, 1 ->
    # 1 -> 0, 1 ->
    #
    def adjlist(self):
        for u, edgelist in self.vertex_weights.items():
            children="->"
            for edge in edgelist:
                for v,w in edge.items():
                    children += " %d, %f ->" % (v, w)
            print("%s %s" % (u, children))
        print()

