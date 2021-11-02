import math
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
        nodes = [x.split(' ')[0].split("\n")[0] for x in open("test.txt").readlines()]
        for i in nodes:
            self.add_vertex(i)
    def read_in_weights(self):
        with open("test1.txt") as file:
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
    
    #following pseudocode from https://www.baeldung.com/cs/tsp-dynamic-programming
    def traveling_salesman_dynamic(self, nodes, starting_node):
        if(starting_node not in self.node_weights):
            print("TSP-D: Invalid Starting Node")
        else:
            visited = {}
            cost = 0
            visited[starting_node] = True
            if(len(nodes) == 2):
                cost = self.node_weights[nodes[0]][nodes[1]]
                return cost
            else:
                unvisited = list(filter((lambda l: l not in visited), nodes))
                currentMin = math.inf
                for i in nodes:
                    for j in unvisited:
                        if(i != j and i != starting_node):
                            new_nodes = nodes.copy()
                            new_nodes.remove(j)
                            cost = min(currentMin, self.traveling_salesman_dynamic(new_nodes, i) + self.node_weights[i][j])
                            visited[i] = True
                            unvisited = list(filter((lambda l: l not in visited), nodes))
        return cost


x = Graph()      
x.read_in_nodes()
x.read_in_weights()
#x.print_graph()
print(x.traveling_salesman_dynamic(list(x.node_weights.keys()), '1'))




