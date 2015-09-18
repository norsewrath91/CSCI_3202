import argparse
import heapq
import math
__author__ = "Nicholas Nocella"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("world", help ="The world matrix you want to use as a .txt file", type=argparse.FileType('r'))
    parser.add_argument("gridHeight", help="The height of your matrix integer vale", type=int)
    parser.add_argument("gridWidth", help="The width of your matrix integer value", type=int)
    parser.add_argument("heuristic", help="Straight Line or Manhattan Distance Heuristic")
    args = parser.parse_args()

    world = args.world
    worldMatrix = []
    for line in world.readlines():
        worldMatrix.append(line.split())

    a = aStar(args.gridHeight,args.gridWidth,worldMatrix, args.heuristic)
    a.initMap()
    a.mainProcess()




class node():
    def __init__(self,y,x,reachable):
        self.x = x
        self.y = y
        self.reachable = reachable
        self.parent = None
        self.g =0
        self.h =0
        self.f =0
        self.diagonal = False


class aStar():
    def __init__(self,height,width,matrix, heuristic):
        self.openedList = []
        heapq.heapify(self.openedList)
        self.closedList = set()
        self.gridHeight = height
        self.gridWidth = width
        self.nodes = []
        self.world = matrix
        self.heuristic = heuristic
        self.totalCost =0


    def initMap(self):
        #takes the matrix given in the command line and creates a list of nodes
        #we only initialize whether or not the node has a mountain (not reachable) or not (reachable)
        for y in range(self.gridHeight):
            for x in range(self.gridWidth):
                self.nodes.append(node(y,x,True))
        for v in self.nodes:
            if self.world[v.y][v.x] == "2":
                v.reachable = False

        self.start = self.getNode((self.gridHeight-1),0)
        self.end = self.getNode(0,(self.gridWidth-1))

    def getNode(self,y,x):
        return self.nodes[y * self.gridWidth + x]

    def displayPath(self):
        print "Total Cost:"
        print self.end.f
        print "The path taken from Start (7 0) to End (0 9):"
        print "Node: (0 9)"
        Node = self.end
        while Node.parent is not self.start:
            Node = Node.parent
            print 'Node: (%d %d)' % (Node.y,Node.x)
        print "Node: (7 0)"


    def manhattanHeuristic(self,Node):
        #computer the heruistic value for a cell, the manhattan distance
        return abs(Node.x - self.end.x) + abs(Node.y - self.end.y)

    def straightLineHeuristic(self,Node):
        return math.sqrt(math.pow((Node.x - self.end.x),2) + math.pow((Node.y-self.end.y),2))

    def getAdjNodes(self,node):
        #Returns adjacent cells in clockwise order starting from right
        #updates if the node if diagonal
        Nodes = []
        if node.x < self.gridWidth-1:
            Nodes.append(self.getNode(node.y,node.x+1))

        if node.x < self.gridWidth-1 and node.y < self.gridHeight-1:
            self.getNode(node.y+1,node.x+1).diagonal = True
            Nodes.append(self.getNode(node.y+1,node.x+1))

        if node.y < self.gridHeight-1:
            Nodes.append(self.getNode(node.y+1,node.x))

        if node.x > 0 and node.y < self.gridHeight-1:
            self.getNode(node.y+1,node.x-1).diagonal = True
            Nodes.append(self.getNode(node.y+1,node.x-1))

        if node.x > 0:
            Nodes.append(self.getNode(node.y,node.x-1))

        if node.x > 0 and node.y > 0:
            self.getNode(node.y-1,node.x-1).daigonal = True
            Nodes.append(self.getNode(node.y-1,node.x-1))

        if node.y > 0:
            Nodes.append(self.getNode(node.y-1,node.x))

        if node.y > 0 and node.x < self.gridWidth-1:
            self.getNode(node.y-1,node.x+1).diagonal = True
            Nodes.append(self.getNode(node.y-1,node.x+1))

        return Nodes

    def updateDiagonalNode(self,adjNode,Node):
            if self.world[adjNode.y][adjNode.x] == "1":
                adjNode.g = Node.g +24
            else:
                adjNode.g = Node.g +14
            if self.heuristic == "manhattan":
                adjNode.h = self.manhattanHeuristic(adjNode)
            elif self.heuristic == "straight":
                adjNode.h = self.straightLineHeuristic(adjNode)
            adjNode.parent = Node
            adjNode.f = adjNode.h + adjNode.g

    def updateNode(self,adjNode,Node):
            if self.world[adjNode.y][adjNode.x] == "1":
                adjNode.g = Node.g +20
            else:
                adjNode.g = Node.g +10
            if self.heuristic == "manhattan":
                adjNode.h = self.manhattanHeuristic(adjNode)
            elif self.heuristic == "straight":
                adjNode.h = self.straightLineHeuristic(adjNode)
            adjNode.parent = Node
            adjNode.f = adjNode.h + adjNode.g

    def mainProcess(self):
        #push starting node to open list
        heapq.heappush(self.openedList,(self.start.f,self.start))
        while len(self.openedList):
            #pop node from queue and add node to closed list
            f, node = heapq.heappop(self.openedList)
            self.closedList.add(node)
            #if we are at the end display the path that got us there
            if node is self.end:
                self.displayPath()
                break
            adjNodes = self.getAdjNodes(node)
            for adjNode in adjNodes:
                if adjNode.reachable != False and adjNode not in self.closedList:
                    if(adjNode.f,adjNode) in self.openedList:
                        if adjNode.diagonal == True:
                            if adjNode.g > node.g +14:
                                self.updateDiagonalNode(adjNode,node)
                        else:
                            if adjNode.g > node.g +10:
                                self.updateNode(adjNode,node)
                    else:
                        if adjNode.diagonal == True:
                            self.updateDiagonalNode(adjNode,node)
                        else:
                            self.updateNode(adjNode,node)
                        heapq.heappush(self.openedList,(adjNode.f,adjNode))
















main()