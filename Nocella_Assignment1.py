__author__ = 'Nick Nocella'

import Queue

#Implement integer queue using python's queue module


#TODO not sure exactly what professor wants for this question

#implement a basic integer stack

class stack ():
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


def main():
    myStack = stack(128)
    myStack.push(12)
    myStack.push(13)
    myStack.checksize()
    myStack.pop()
    myStack.checksize()

main()