__author__ = 'Nick Nocella'

import Queue

#Implement integer queue using python's queue module





#implement a basic integer stack

class stack:
    def __init__(self, maxsize):
        if maxsize <= 0:
            self.maxsize = 128
        else:
            self.maxsize = maxsize
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True

    def isFull(self):
        if len(self.data) == self.maxsize:
            return True

    def push(self, integer):
        if not self.isFull():
            self.data.append(integer)
            print "%d has been pushed to the stack" %integer


    def pop(self):
        if not self.isEmpty():
            popped = len(self.data)-1
            del self.data[len(self.data)-1]
            print "%d has been popped off the stack" %popped


    def checksize(self):
        print "The size of the stack is %d" %len(self.data)

#implement a binary tree

class node:
    def __init__(self, integer):
        self.left = None
        self.right = None
        self.parent = None
        self.key = integer

class bTree:
    def __init__(self,integer):
        self.root = node(integer)

    def search(self,integer):
        Node = self.root
        while Node !=None:
            if Node.key == integer:
                return Node
            if Node.key > integer:
                Node = Node.left
            else:
                Node = Node.right
        return None

    def add(self, integer, parent):
        Node = self.search(parent)
        if Node != None:
            self._add(integer,Node)
        else:
            print "Parent not Found"

    def _add(self, integer, Node):
        if(integer < Node.key):
            if(Node.left != None):
                print "Parent already has left child"
            else:
                Node.left = node(integer)
        else:
            if(Node.right != None):
                print "Parent already has right child"
            else:
                Node.right = node(integer)
    def delete(self,integer):
        Node = self.search(integer)
        if Node != None:
            if(Node.right == None and Node.left == None):
                Node.key = None
            else:
                print "Node not deleted has children"
        else:
            print "Node not found"

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, Node):
        if(Node != None):
            self._printTree(Node.left)
            print str(Node.key) + ' '
            self._printTree(Node.right)

#Implement a unweighted graph using dictionary

class graph:
    def __init__(self):
        self.start = {}

    def addVertex(self,integer):
        if self.start.has_key(integer):
            print "Vertex already exists"
        else:
            self.start.update({integer: []})

    def addEdge(self,integer1, integer2):
        if self.start.has_key(integer1) and self.start.has_key(integer2):
            self.start[integer1].append(integer2)
            self.start[integer2].append(integer1)

        else:
            print "One or more vertices not found"

    def findVertex(self,integer):
        if self.start.has_key(integer):
            print self.start.get(integer)


def main():

    #test queue
    print "Testing queue module"
    myQueue = Queue.Queue()
    list = [1,2,3,4,5,6,7,8,9,10]
    for integer in list:
        myQueue.put(integer)
    for integer in range(1,11):
        print myQueue.get(integer)

    #test stack
    print "Testing stack class"
    myStack = stack(20)
    for integer in list:
        myStack.push(integer)
    for integer in range(1,11):
        myStack.pop()


    #test bTree
    myBTree = bTree(1)
    myBTree.add(3,1)
    myBTree.add(2,1)
    myBTree.add(5,2)
    myBTree.add(1,2)


    #test graph
    print "Testing graph class"
    myGraph = graph()
    for integer in list:
        myGraph.addVertex(integer)
    myGraph.addEdge(1,2)
    myGraph.addEdge(1,3)
    myGraph.addEdge(1,4)
    myGraph.addEdge(2,3)
    myGraph.addEdge(2,5)
    myGraph.addEdge(2,9)
    myGraph.addEdge(3,7)
    myGraph.addEdge(3,10)
    myGraph.addEdge(4,6)
    myGraph.addEdge(5,6)
    myGraph.addEdge(5,6)
    myGraph.addEdge(5,7)
    myGraph.addEdge(6,9)
    myGraph.addEdge(9,10)
    myGraph.addEdge(9,1)
    myGraph.addEdge(7,8)
    myGraph.addEdge(8,9)
    myGraph.addEdge(8,1)
    myGraph.addEdge(8,2)
    myGraph.addEdge(8,4)
    print myGraph.start

    for integer in range(1,6):
        myGraph.findVertex(integer)


main()
