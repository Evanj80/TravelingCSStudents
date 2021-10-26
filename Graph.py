from collections import defaultdict
class Graph:
    node_weights = defaultdict(lambda : [])
    number_of_nodes = 0
    
    def Graph(self):
        self.node_weights = {}
        self.number_of_nodes = 0
    
    def addVertex(self,x):
        if x in self.node_weights:
            return -1
        else:
            self.node_weights[x] = []
            self.number_of_nodes += 1

    def addEdge(self,v1,v2,edge_weight):
        self.node_weights[v1].append({v2:edge_weight})
            
    def print_graph(self):
        for i in self.node_weights.items():
            print(i)
            
    def readInNodes(self):
        nodes = [x.split(' ')[0] for x in open("test1.txt").readlines()]
        for i in nodes:
            self.addVertex(i)
    def readInWeights(self):
        with open("test.txt") as file:
            for line in file:
                line = line.split(" ")
                starting_node = line[1]
                # print(starting_node)
                end_node = line[2]
                # print(end_node)
                weight_between = line[3]
                weight_between = weight_between[:-1]
                # print(weight_between)
                self.addEdge(starting_node,end_node,weight_between)
        # print(self.node_weights)


        
x = Graph()      
x.readInNodes()
x.readInWeights()
x.print_graph()



