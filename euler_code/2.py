import sys

""""
CSCI3220 2018-19 First Term Assignment 2
I declare that the assignment here submitted is original except for source
material explicitly acknowledged, and that the same or closely related material
has not been previously submitted for another course. I also acknowledge that I
am aware of University policy and regulations on honesty in academic work, and
of the disciplinary guidelines and procedures applicable to breaches of such
policy and regulations, as contained in the following websites.
University Guideline on Academic Honesty:
http://www.cuhk.edu.hk/policy/academichonesty/
Student Name: Nigel Nicholas
Student ID : 1155088791
"""


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                                           Class for Creating Object Graph

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

#- - - - - - - - - - - - 
#Function add_node
#Input = character: string
#Output = none

#Create a new object Node if it hasn't existed yet
#Add character into the list of characters that already exist
#Insert the new node into into list of nodes in the graph and map the node object to a certain index
#- - - - - - - - - - - - - - 
    def add_node(self, character):
        # if node with such character exists, return
        if character in self.character_list:
            return

        newnode = Nodes(character)
        self.vertex_list.append(newnode)
        self.character_list.append(character)
        self.position_in_list[character] = self.index
        self.index = self.index + 1

#- - - - - - - - - - 
#Function add_edge
#Input = input1:string  ,  input2: string,      weight: string  
#Output = __

#Create a new edge that connects input1->input2 ( directed edge )
#Store it in a list of edges in the graph
#Update indegree and outdegree 
#- - - - - - - - - - 

    def add_edge(self, char1, char2, weight):   
        u = self.vertex_list[self.position_in_list[char1]]    # u is node object
        v = self.vertex_list[self.position_in_list[char2]]    # v is node object
        newEdge = Edge(u, v, weight) # Here take assumption that weight is 1 to make everything uniform
        self.edge_list.append(newEdge)
        u.adjacent_vertices.append(v)
        u.edges.append(newEdge)
        v.indegree += 1
        u.outdegree += 1

#- - - - - - - - - - - - - - - - 
# Function find_start
# Input: __
# Output: obj: type Node

# Traverse through all the vertex and find one with more outdegree than indegree, if not select any of nodes
# Assumption : The graph always has eulerian path and therefore always gives valid requirement for Eulerian Path
# 
#- - - - - - - - - - - - - - - - 

    def find_start(self):
        # Finding the node that has >0 outdeg-indeg
        for vertex in self.vertex_list:
            if vertex.outdegree - vertex.indegree == 1:
                return vertex
        
        # By the time you got here, then there are no vertex with out-in = 1

        return self.vertex_list[0]

#- - - - - - - - - - - - - - - - -
# Function euler
# Input = start : type Node; 
# Output = __ 

# Function that fills in the eulerian path stack and moves around current_path
# Algorithm :
# Keep track of the current path , for every node visited , push it to the stack
# If at some point you're stuck push the current path into the eulerian path stack

#- - - - - - - - - - - - - - - - 

    
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
        return
    
#- - - - - - - - - - - - - - - - 
# Function print_euler
# Input : Graph Object of the caller
# Output : Result:string

# From the euler_path stack, reverse the stack then print accordingly
# Take the first full string then keep appending last element of each node.string

#- - - - - - - - - - - - - - - - 

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


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                                       Class for Creating Node Object
class Nodes(object):

    def __init__(self,alphabet):
        self.indegree = 0 
        self.outdegree = 0 
        self.adjacent_vertices = [] # You can store edge objects here
        self.content = alphabet
        self.edges = []


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                                       Class for Creating Edge Object
class Edge(object):
    # u is the initial node
    # v is the target node
    def __init__(self, node1, node2, weight):
        self.u = node1  
        self.v = node2
        self.weight = weight


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                                       Main Function to put the prompt in

G = Graph()

# prompt
codon = raw_input()

while bool(codon) :
    # divide codon into k-1 prefix and k-1 suffix
    prefix = codon[:len(codon)-1]
    suffix = codon[1:]
    G.add_node(prefix)
    G.add_node(suffix)

    G.add_edge(prefix, suffix, codon)

    try:
        codon = raw_input()
    except(EOFError):
        break

sys.setrecursionlimit(1500)

# Commands to run in ordcer to do the eulerian path
start = G.find_start()
G.euler(start)
G.print_euler()