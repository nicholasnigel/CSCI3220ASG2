
class Edge(object):
    # u is the initial node
    # v is the target node
    def __init__(self, node1, node2, weight):
        self.u = node1  
        self.v = node2
        self.weight = weight