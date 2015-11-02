__author__ = 'Nick'


class node():
    def __init__(self, name):
<<<<<<< Updated upstream
        self.prob = {}
        self.parents = None
        self.children = None
=======
        self.probabilities = {}
        self.parents = []
>>>>>>> Stashed changes
        self.name = name

class network:
    def __init__(self):
        self.start = {}

    def addVertex(self,node):
            self.start.update({node: []})

    def addEdge(self,node1, node2):
        if self.start.has_key(node1) and self.start.has_key(node2):
            self.start[node1] = node2

    def findVertex(self,node):
        if self.start.has_key(node):
<<<<<<< Updated upstream
            print self.start.get(node)
=======
            print self.start.get(node)
>>>>>>> Stashed changes
