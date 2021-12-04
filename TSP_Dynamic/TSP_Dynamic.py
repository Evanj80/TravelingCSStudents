import math
import geopy.distance
import psutil
import os
import time
import sys

# graph object using array implementation
class Graph:
    number_of_nodes = 0
    nodes = {}

    def __init__(self, initialValue = -1, filename ="test.txt"):
        self.read_in_nodes(filename)
        self.graph = [[float(initialValue)]*self.number_of_nodes] * self.number_of_nodes


    def read_in_nodes(self, filename="test.txt"):
        with open(os.path.join(os.sys.path[0], filename)) as file:
            i = 0
            for line in file:
                split = line.split()
                if(split[0].isnumeric()):
                    self.nodes[split[0]] = (i, float(split[1]), float(split[2]))
                    self.number_of_nodes += 1
                    i = i+1
    
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

    def generate_edge_weights(self):
        for i in self.nodes.keys():
            for j in self.nodes.keys():
                if( i != j):
                    coords1 = (self.nodes[i][1], self.nodes[i][2])
                    coords2 = (self.nodes[j][1], self.nodes[j][2])
                    self.graph[self.nodes[i][0]][self.nodes[j][0]] = geopy.distance.distance(coords1, coords2).km
    
    def get_edge_weight(self, v1, v2):
        weight = self.graph[self.nodes[v1][0]][self.nodes[v2][0]]
        if (weight != -1):
            return weight
    
# formula: TSP(s,G) = min(C(s,k) + TSP(k, G-{k})) for all k in G not equal to s
def TSP_dynamic(graph, nodes, starting_node, original_start, file = None, calculated={}):
    if(starting_node not in nodes):
        print("TSP-D: Invalid Starting Node")
        print("Node: ", starting_node)
        print("Nodes: ", nodes)
    else:
        # initialize the path and remove the current node from the unvisited nodes list
        path = [starting_node]
        unvisited = nodes.copy()
        unvisited.remove(starting_node)

        # check if this subproblem has already been solved
        identifier = str(starting_node) + '-' + str(unvisited)
        if (identifier in calculated.keys()):
            return calculated[identifier]

        # if there is only 1 unvisited node, add the original starting node to the end of the path and return the cost of going abck to the start
        if(len(unvisited) == 0):
            path.append(original_start)
            return (graph.get_edge_weight(starting_node, original_start), path)
        else:
            # for each unvisited node, call TSP again, and keep track of which one has the lowest cost
            currentMin = math.inf
            currentMinPath = []
            for i in unvisited:
                tsp = TSP_dynamic(graph, unvisited, i, original_start, file, calculated)
                cost = graph.get_edge_weight(starting_node, i) + tsp[0]
                if(cost < currentMin):
                    currentMin = cost
                    currentMinPath = tsp[1]
        # append the found lowest cost path to the end of the current path, save the result, and return the path and it's cost
        path = path + currentMinPath
        calculated[identifier] = (currentMin, path)
        return (currentMin, path)

# Driver code
sys.setrecursionlimit(5000)

file = open(os.path.join(os.sys.path[0], "TSP_Dynamic_Data.txt"), "w")
pathFile = open(os.path.join(os.sys.path[0], "TSP_Dynamic_Output.csv"), "w")

x = Graph(10000, "bulgaria.tsp")

start = time.time()
x.generate_edge_weights()
end = time.time()

file.write("took " + str(end-start) + " seconds to generate edges\n")
file.write("Graph takes " + str(sys.getsizeof(x.graph)) + " bytes\n")

start = time.time()
result = TSP_dynamic(x, list(x.nodes.keys()), '1', '1')
end = time.time()

for i in result[1]:
    pathFile.write(str(i) + "," + str(x.nodes[i][1]) + "," + str(x.nodes[i][2]) + "\n")

file.write("TSP_Dynamic took " +  str(end-start) + " seconds and used " +  str(psutil.Process().memory_info().peak_wset / (1024 ** 2)) + "Mb of memory\n")
file.write("path weight: " + str(result[0]) + "\n")

print("path weight: " + str(result[0]) + "\n")

file.close()
pathFile.close()
