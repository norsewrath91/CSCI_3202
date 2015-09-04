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
        return self._search(integer,self.root)

    def _search(self,integer,Node):

         if Node.key == integer:
            return Node
         else:
            if Node.left is not None:
               return self._search(integer, Node.left)
            if Node.right is not None:
                return self._search(integer,Node.right)


    def add(self, integer, parent):
        Node = self.search(parent)
        if Node != None:
            self._add(integer,Node)
        else:
            print "Parent not Found"

    def _add(self, integer, Node):
        if(Node.left == None):
            Node.left = node(integer)
        elif(Node.left != None and Node.right == None):
            Node.right = node(integer)
        else:
            print "Parent already has two children"



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
    print "Testing Btree"
    myBTree = bTree(1)
    myBTree.add(3,1)
    myBTree.add(4,1)
    #check add to parent node with two children
    myBTree.add(5,1)
    #check add to a none existing parent node
    myBTree.add(9,10)
    #check add to children nodes
    myBTree.add(5,3)
    myBTree.add(6,3)
    myBTree.add(12,5)
    myBTree.add(14,5)
    myBTree.add(13,12)
    myBTree.add(22,13)
    myBTree.add(20,13)
    myBTree.printTree()
    myBTree.delete(20)
    myBTree.delete(22)
    myBTree.printTree()



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
    myGraph.addEdge(5,10)
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
