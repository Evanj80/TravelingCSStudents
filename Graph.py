from collections import defaultdict
class Graph:
    verticesfile = ""
    edgesfile = ""
    vertex_weights = defaultdict(lambda : [])
    number_of_vertices = 0
    
    def __init__(self, vf="", ef=""):
        self.verticesfile = vf
        self.edgesfile = ef
        self.vertex_weights = {}
        self.number_of_vertices = 0
        if (len(self.verticesfile) > 0 and len(self.edgesfile) > 0):
            self.readInVertices()
            self.readInWeights()
    
    def addVertex(self,x):
        if x in self.vertex_weights:
            return -1
        else:
            self.vertex_weights[x] = []
            self.number_of_vertices += 1

    def addEdge(self,v1,v2,edge_weight):
        self.vertex_weights[v1].append({v2:edge_weight})
            
    def print_graph(self):
        for i in self.vertex_weights.items():
            print(i)
            
    def readInVertices(self):
        vertices = [x.replace("\n","").split(' ')[0] for x in open(self.verticesfile).readlines()]
        for i in vertices:
            self.addVertex(int(i))

    def readInWeights(self):
        with open(self.edgesfile) as file:
            for line in file:
                line = line.split(" ")
                starting_vertex = int(line[1])
                end_vertex = int(line[2])
                weight_between = float(line[3])
                self.addEdge(starting_vertex,end_vertex,weight_between)
        # print(self.vertex_weights)

    # Find vertices that have no edges
    def fixInput(self):
        for original in self.vertex_weights:
            x=[]
            #Look at the existing connections and add them to a list temp
            for vertex in self.vertex_weights[original]:
                # Only keep the vertex we dont care about weight
                x.append(vertex)
            # Visit exisitng vertices and see if they are in list    
            for f in self.vertex_weights.keys():
                # If they are not and are not the same as our original node,
                # add them with huge weight
                if(f not in x and original != f):
                    self.addEdge(original,f,1000)          

