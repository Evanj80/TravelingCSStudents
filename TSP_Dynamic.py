import math
import os
from collections import defaultdict
from itertools import permutations

class Graph:
    node_weights = defaultdict(lambda : [])
    number_of_nodes = 0
    
    def Graph(self):
        self.node_weights = {}
        self.number_of_nodes = 0
    
    def add_vertex(self,x):
        if x in self.node_weights:
            return -1
        else:
            self.node_weights[x] = {}
            self.number_of_nodes += 1

    def add_edge(self,v1,v2,edge_weight):
        self.node_weights[v1][v2] = float(edge_weight)
            
    def print_graph(self):
        for i in self.node_weights.keys():
            print(i + ': ' + str(self.node_weights[i]))
            
    def read_in_nodes(self):
        nodes = [x.split(' ')[0].split("\n")[0] for x in open(os.path.join(os.sys.path[0], "test.txt")).readlines()]
        for i in nodes:
            self.add_vertex(i)

    def read_in_weights(self):
        with open(os.path.join(os.sys.path[0], "test1.txt")) as file:
            for line in file:
                line = line.split(" ")
                starting_node = line[1]
                # print(starting_node)
                end_node = line[2]
                # print(end_node)
                weight_between = line[3]
                weight_between = weight_between[:-1]
                # print(weight_between)
                self.add_edge(starting_node,end_node,weight_between)
        # print(self.node_weights)
    
    #formula: TSP(s,G) = min(C(s,k) + TSP(k, G-{k})) for all k in G not equal to s
    def TSP_dynamic(self, nodes, starting_node, original_start):
        if(starting_node not in self.node_weights):
            print("TSP-D: Invalid Starting Node")
        else:
            path = []
            path.append(starting_node)
            if(starting_node in nodes):
                nodes = nodes.copy()
                nodes.remove(starting_node)
            if(len(nodes) == 0):
                path.append(original_start)
                return (self.node_weights[starting_node][original_start], path)
            else:
                currentMin = math.inf
                currentMinPath = []
                for i in nodes:
                    tsp = self.TSP_dynamic(nodes, i, original_start)
                    cost = self.node_weights[starting_node][i] + tsp[0]
                    if(cost < currentMin):
                        currentMin = cost
                        currentMinPath = tsp[1]
        path = path + currentMinPath
        return (currentMin, path)



x = Graph()      
x.read_in_nodes()
x.read_in_weights()
#x.print_graph()
print(x.TSP_dynamic(list(x.node_weights.keys()), '1', '1'))
