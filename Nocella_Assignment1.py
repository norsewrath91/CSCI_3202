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
        self.intKey = integer

class bTree:
    def __init__(self,integer):
        #the way the assignmnet is written it seems you should not be able to instantiate an empty btree unless you want constant parent not found messages :P
        self.root = node(integer)
    def search(self,integer):
        self._search(integer,self.root)

    def _search(self, integer, node):
        if (integer == node.intKey):
            return node
        elif (integer < node.intKey and node.left != None):
            self._search(integer, node.left)
        elif (integer > node.intKey and node.right !=None):
            self._search(integer, node.right)

    def add(self,integer, parent):
        if self.search(parent) != None:
             self._add(integer, node)
        else:
            print "Parent not found"
    def _add(self, integer, node):
        if (integer < node.intKey):














def main():
    myStack = stack(128)
    myStack.push(12)
    myStack.push(13)
    myStack.checksize()
    myStack.pop()
    myStack.checksize()

main()