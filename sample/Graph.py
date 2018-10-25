# This is the data structure of a graph by python
from Nodes import Nodes
from Edge import Edge
import itertools
# This is assuming that the graph is directed
# Each graph contains list of nodes and its corresponding vertices
# For each graph, there should be list of nodes, then a dictionary to keep vertices
# if it is a weighted graph, how would you store the weight on edges

class Graph(object):

    def __init__(self):
        self.vertex_list = []   # The list should contain Node objects 
        self.edge_list = []
        self.index = 0
        self.position_in_list = {}
        self.character_list = [] # List of the characters, like A B C D E, to see if such node has been created
        self.visited_edge = []  # keep track of visited_edge
        self.current_path = []  # stack for tracking the visting edges 
        self.eulerian_path = [] # stack for storing the eulerian path


    def add_node(self, character):
        # if node with such character exists, return
        if character in self.character_list:
            return

        newnode = Nodes(character)
        self.vertex_list.append(newnode)
        self.character_list.append(character)
        self.position_in_list[character] = self.index
        self.index = self.index + 1

    def add_edge(self, char1, char2, weight):   
        u = self.vertex_list[self.position_in_list[char1]]    # u is node object
        v = self.vertex_list[self.position_in_list[char2]]    # v is node object
        newEdge = Edge(u, v, weight) # Here take assumption that weight is 1 to make everything uniform
        self.edge_list.append(newEdge)
        u.adjacent_vertices.append(v)
        u.edges.append(newEdge)
        v.indegree += 1
        u.outdegree += 1

    def find_start(self):
        # Finding the node that has >0 outdeg-indeg
        for vertex in self.vertex_list:
            if vertex.outdegree - vertex.indegree ==1 :
                return vertex
        
        # By the time you got here, then there are no vertex with out-in = 1

        return self.vertex_list[0]
    
    def euler(self, start):
        # start is of type: Nodes
        self.current_path.append(start)
        for edges in start.edges:
            if edges in self.visited_edge:
                continue
            self.visited_edge.append(edges)
            self.euler(edges.v) # if no edges then this line will be passed
        self.eulerian_path.append(self.current_path[-1])
        self.current_path.pop()
        if not self.visited_edge:
            self.visited_edge.pop()
        return

    def euler_bonus(self,start):
        # instead of using self.eulerian path, then use path for every recursion call
        for edgelist in list(itertools.permutations(start.edges)) :
            self.current_path.append(start)
            for edges in edgelist:
                if edges in self.visited_edge:
                    continue
                self.visited_edge.append(edges)
                self.euler(edges.v)
            # in here then there are no more edges to traverse therefore it can return now, then remove visited edge
            self.eulerian_path.append(self.current_path[-1])
            if len(self.eulerian_path) == len(self.edge_list):
                self.print_euler()
            
            self.current_path.pop()
            if not self.visited_edge:
                self.visited_edge.pop()
            return
        


    
    def print_euler(self):
        
        eulerpath = self.eulerian_path[-1].content
        self.eulerian_path.pop()
        self.eulerian_path.reverse()
        # get all string in index 0 
        # then print the last char for all string in index 1-> len-1
        
        for nodes in self.eulerian_path:
            eulerpath = eulerpath + nodes.content[-1]
        
        print eulerpath
        return eulerpath




