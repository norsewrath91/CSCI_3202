__author__ = 'Nick Nocella'

import Queue

#Implement integer queue using python's queue module


#TODO not sure exactly what professor wants for this question

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







def main():
    myStack = stack(128)
    myStack.push(12)
    myStack.push(13)
    myStack.checksize()
    myStack.pop()
    myStack.checksize()
    tree = bTree(2)
    tree.add(5,2)
    tree.add(1,2)
    tree.add(6,2)
    tree.add(1,2)
    tree.delete(1)
    tree.printTree()


main()
