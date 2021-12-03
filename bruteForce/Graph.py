from collections import defaultdict
from itertools import permutations
from typing import List
import geopy.distance
import timeit

from shapely.impl import DefaultImplementation


class Graph:
    #Actual # of nodes
    number_of_nodes = 0
    #All nodes coordinates
    node_list = defaultdict(lambda: [])
    #PreProcessed distances 
    preProcessed = defaultdict(lambda: {})
    
    def Graph(self):
        self.number_of_nodes = 0
        self.node_list = {}
        self.preProcessed = {}
    
    #Writes this data to the node list that keeps track of everyones coordinates
    def add_vertex(self,x):
        self.number_of_nodes += 1
        self.node_list[x[0]]=[x[1],x[2]]

    #Reads in nodes and seperates them in [[longitude,latitude],.......]
    def read_in_nodes(self):
        nodes = [x.split(' ') for x in open("bulgaria.tsp").readlines()]
        for i in nodes:
            self.add_vertex(i)
    
    #Writes results to files for later mapping
    def write_path(self,list_final,runtime):
        print(list_final)
        f = open("resultsBruteForce.csv", "w")
        f.write("Long,Lat")
        f.write("\n")
        for i in list_final:
            x = list(i)
            coords = self.node_list[x[0]]
            f.write(f'{coords[0]},{coords[1]}')
            f.write("\n")
        f.write("\n")
        s = open("timeBruteForce.txt", "w")
        s.write(str(runtime))
        f.close()
        s.close()
    
    
    def preProcessData(self):
        # for every node calculate its distance to every other node.
        for i in self.node_list:
            starting_point = i
            #Save first node and calc dist to everyone else in for loop below
            starting_coords_1 = (float(self.node_list[starting_point][0]), float(self.node_list[starting_point][1]))
            for j in self.node_list:
                distance = 0
                ending_coords_2 = (float(self.node_list[j][0]), float(self.node_list[j][1])) 
                distance= geopy.distance.geodesic(starting_coords_1, ending_coords_2).km
                #Store distances in preprocessed dict for later
                self.preProcessed[i].update({j:distance})

    def traveling_salesman_brute_force(self):
        start_time = (float)(timeit.default_timer())
        optimal = 0
        #calculate all permmuations possible
        all_pos = list(permutations(self.node_list.keys()))
        print(len(all_pos))
        #Set insanely high current low to start to that alg can start comparing overall 
        #path lengths
        current_low=100000000000
        final_list = []
        for i in all_pos:
            starting_point = i[0]
            start = i[0]
            #Temp list to hold potential most optimal path
            path_list=[]
            path_list.append(starting_point)
            #start at first node in current permuation 
            for z in i[1:]:
                #loop through rest of permuation
                optimal+= self.preProcessed[starting_point][z]
                path_list.append(z)
                starting_point = z
            #Then add the path way back to go to where you started.
            optimal+= self.preProcessed[start][starting_point]
            path_list.append(start)
            #If current permuation is better than all before it, save its path and 
            #distance value 
            if current_low>optimal:
                current_low = optimal
                final_list = path_list
            
            optimal = 0
        stop = timeit.default_timer()
        runtime=(float)(stop-start_time)
        self.write_path(final_list, runtime)
        return current_low

    # edgeswriter produces an edges file for the dataset
    # edges file format
    # i u v w
    #
    # i = line number
    # u = source
    # v = destination
    # w = weight calculated with geopy.distance
    def edgeswriter(self):
        f = open("bulgaria-edges.tsp","w")
        # n(n-1)/2 edges in a complete graph
        maxedges = int((self.number_of_nodes*(self.number_of_nodes-1)) / 2 )
        i = 0
        for u in range(1,self.number_of_nodes+1):
            for v in range(1,self.number_of_nodes+1):
                # distance between coordinates
                w = geopy.distance.geodesic(
                    (self.node_list[str(u-0)][0],self.node_list[str(u-0)][1]),
                    (self.node_list[str(v-0)][0],self.node_list[str(v-0)][1])
                ).km
                #print("%d %d %d %f" %(i,u,v,w)) 
                if (u != v):
                    f.write("%d %d %d %f\n" %(i,u,v,w)) 
                i+=1
        
x = Graph()      
x.read_in_nodes()
x.preProcessData()
print(x.traveling_salesman_brute_force())



x.edgeswriter()
#print(x.traveling_salesman_brute_force())

