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
            self.node_weights[x] = []
            self.number_of_nodes += 1

    def add_edge(self,v1,v2,edge_weight):
        self.node_weights[v1].append((v2,edge_weight))
            
    def print_graph(self):
        for i in self.node_weights.items():
            print(i)
            
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

    def traveling_salesman_brute_force(self):
        optimal = 0
        all_pos = list(permutations(self.node_weights.keys()))
        current_low=100000000000
        for i in all_pos:
            starting_point = i[0]
            # print(i)
            neighbors = self.node_weights[starting_point]
            # print(neighbors)
            for z in i[1:]:

                optimal += (float)((dict(neighbors)[z]))
                neighbors = self.node_weights[z]
                last_known_node = z
            final_value = dict(self.node_weights[last_known_node])[starting_point]
            optimal += float(final_value)
 
            # print(optimal)
            if current_low>optimal:
                current_low = optimal
            optimal = 0
             
        return current_low



        
        
x = Graph()      
x.read_in_nodes()
x.read_in_weights()
x.print_graph()
print(x.traveling_salesman_brute_force())




