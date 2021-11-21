import math
import os
import time
import sys
from collections import defaultdict
from itertools import permutations

class Graph_Array:
    number_of_nodes = 0
    nodes = {}
    def __init__(self, initialValue = -1, filename ="test.txt"):
        self.read_in_nodes(filename)
        self.graph = [[initialValue]*self.number_of_nodes] * self.number_of_nodes

    def read_in_nodes(self, filename="test.txt"):
        nodes = [x.split(' ')[0].split("\n")[0] for x in open(os.path.join(os.sys.path[0], filename)).readlines()]
        
        for i in nodes:
            if(i.isnumeric()):
                self.nodes[i] = self.number_of_nodes
                self.number_of_nodes += 1
    
    def read_in_edges(self, filename="test1.txt"):
        with open(os.path.join(os.sys.path[0], filename)) as file:
            for line in file:
                line = line.split(" ")
                if(not line[1].isnumeric()):
                    continue
                starting_node = line[1]
                end_node = line[2]
                weight = line[3]
                weight = weight[:-1]
                self.graph[self.nodes[starting_node]][self.nodes[end_node]] = float(weight)
    
    def get_edge_weight(self, v1, v2):
        weight = self.graph[self.nodes[v1]][self.nodes[v2]]
        if (weight != -1):
            return weight

class Graph:
    node_weights = {}
    number_of_nodes = 0
    number_of_edges = 0
    node_list = []
    
    def Graph(self):
        self.node_weights = {}
        self.number_of_nodes = 0
        self.node_list = []
    
    def add_vertex(self,x):
        if x in self.node_weights:
            return -1
        else:
            self.node_weights[x] = {}
            self.number_of_nodes += 1
            self.node_list.append(x)

    def add_edge(self,v1,v2,edge_weight):
        self.number_of_edges += 1
        self.node_weights[v1][v2] = float(edge_weight)

    def get_edge_weight(self, v1, v2):
        return self.node_weights[v1][v2]
            
    def print_graph(self):
        for i in self.node_weights.keys():
            print(i + ': ' + str(self.node_weights[i]))
            
    def read_in_nodes(self, filename="test.txt"):
        nodes = [x.split(' ')[0].split("\n")[0] for x in open(os.path.join(os.sys.path[0], filename)).readlines()]
        for i in nodes:
            if(i.isnumeric()):
                self.add_vertex(i)

    def fixInput(self):
        for original_node in self.node_weights:
            x=[]
            #Look at the existing connections and add them to a list temp
            for node in self.node_weights[original_node]:
                #Only keep the node we dont care about weight
                x.append(node[0])
            #Go through all exisitng nodes in problem and see if they are in list    
            for f in self.node_list:
                #If they are not and are not the same as our original node add them with huge weight
                if(f not in x and original_node != f):
                    self.add_edge(original_node,f,1000000) 
      
    def read_in_weights(self, filename="test1.txt"):
        with open(os.path.join(os.sys.path[0], filename)) as file:
            for line in file:
                line = line.split(" ")
                if(not line[1].isnumeric()):
                    continue
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
def TSP_dynamic(graph, nodes, starting_node, original_start, calculated={}):
    if(starting_node not in nodes):
        print("TSP-D: Invalid Starting Node")
        print("Node: ", starting_node)
        print("Nodes: ", nodes)
    else:
        path = []
        path.append(starting_node)
        if(starting_node in nodes):
            nodes = nodes.copy()
            nodes.remove(starting_node)

        identifier = str(starting_node) + '-' + str(nodes)
        if (identifier in calculated.keys()):
            return calculated[identifier]

        if(len(nodes) == 0):
            path.append(original_start)
            return (graph.get_edge_weight(starting_node, original_start), path)
        else:
            currentMin = math.inf
            currentMinPath = []
            for i in nodes:
                tsp = TSP_dynamic(graph, nodes, i, original_start, calculated)
                cost = graph.get_edge_weight(starting_node, i) + tsp[0]
                if(cost < currentMin):
                    currentMin = cost
                    currentMinPath = tsp[1]
        path = path + currentMinPath
        calculated[identifier] = (currentMin, path)
        return (currentMin, path)

"""
x = Graph()      
start = time.time()
x.read_in_nodes()
end = time.time()
print(x.number_of_nodes, " nodes, took ", end-start, " seconds to read")
start = time.time()
x.read_in_weights()
end = time.time()
print(x.number_of_edges, " edges, took ", end-start, " seconds to read")
x.fixInput()
print("Graph read, performing TSP using dynamic Programming")
"""

sys.setrecursionlimit(200000)
x = Graph_Array(10000, "Nodes.txt")
x.read_in_edges("edge_weights.txt")

print(TSP_dynamic(x, list(x.nodes.keys()), '1', '1'))
