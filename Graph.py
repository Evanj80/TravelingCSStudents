from collections import defaultdict
from itertools import permutations
from typing import List
import geopy.distance
import timeit


class Graph:
    node_weights = defaultdict(lambda : [])
    number_of_nodes = 0
    node_list = defaultdict(lambda: [])
    
    def Graph(self):
        # self.node_weights = {}
        self.number_of_nodes = 0
        self.node_list = {}
    
    def add_vertex(self,x):
        if x[0] in self.node_weights:
            return -1
        else:
            # self.node_weights[x[0]] = []
            self.number_of_nodes += 1
            self.node_list[x[0]]=[x[1],x[2]]
            print(self.node_list)

    # def fixInput(self):
    #     for original_node in self.node_weights:
    #         x=[]
    #         #Look at the existing connections and add them to a list temp
    #         for node in self.node_weights[original_node]:
    #             #Only keep the node we dont care about weight
    #             x.append(node[0])
    #         #Go through all exisitng nodes in problem and see if they are in list    
    #         for f in self.node_list:
    #             #If they are not and are not the same as our original node add them with huge weight
    #             if(f not in x and original_node != f):
    #                 self.add_edge(original_node,f,1000000)          


    # def add_edge(self,v1,v2,edge_weight):
    #     self.node_weights[v1].append((v2,edge_weight))
            
    # def print_graph(self):
    #     for i in self.node_weights.items():
    #         print(i)
                
            
    def read_in_nodes(self):
        nodes = [x.replace("\n","").split(' ') for x in open("bulgaria.tsp").readlines()]
        print(nodes)
        for i in nodes:
            self.add_vertex(i)
    

    def write_path(self,list_final,runtime):
        f = open("resultsBruteForce.txt", "w")
        for i in list_final:
            x = list(i)
            f.write(f'{x[0]},')
        f.write("\n")
        f.write(str(runtime))
        f.close()

    def traveling_salesman_brute_force(self):
        start_time = (float)(timeit.default_timer())
        optimal = 0
        all_pos = list(permutations(self.node_list.keys()))
        current_low=100000000000
        path_list = []
        final_list = []
        for i in all_pos:
            starting_point = i[0]
            #preserve starting point bad variable name tbh
            start = i[0]
            # print(i)
            # print(neighbors)
            path_list=[]
            for z in i[1:]:
                starting_coords_1 = (float(self.node_list[starting_point][0]), float(self.node_list[starting_point][1]))
                ending_coords_2 = (float(self.node_list[z][0]), float(self.node_list[starting_point][1]))
                optimal+= geopy.distance.geodesic(starting_coords_1, ending_coords_2).km
                path_list.append(starting_point)
                starting_point = z
            starting_coords_1 = (float(self.node_list[starting_point][0]), float(self.node_list[starting_point][1]))
            ending_coords_2 = (float(self.node_list[start][0]), float(self.node_list[start][1]))
            optimal+= geopy.distance.geodesic(starting_coords_1, ending_coords_2).km
            path_list.append(starting_point)
            # print(optimal)
            if current_low>optimal:
                current_low = optimal
                final_list = path_list
            
            optimal = 0
        stop = timeit.default_timer()
        runtime=(float)(stop-start_time)
        self.write_path(final_list, runtime)
        return current_low








        
        
x = Graph()      
x.read_in_nodes()
# x.read_in_weights()
# x.fixInput()
# x.print_graph()
print(x.traveling_salesman_brute_force())




