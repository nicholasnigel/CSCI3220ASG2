# Code for class nodes (used in a graph)

class Nodes(object):

    def __init__(self,alphabet):
        self.indegree = 0 
        self.outdegree = 0 
        self.adjacent_vertices = [] # You can store edge objects here
        self.content = alphabet
        self.edges = []


    

