

__author__ = 'Nick'



class bayesNetwork():
    def __init__(self):
        #initialize our network and nodes with probabilities
        self.net = network()

        self.P = node('P')
        self.C = node('C')
        self.S = node('S')
        self.X = node('X')
        self.D = node('D')

        self.P.prob = {'P':.9,'p':.1}
        self.P.children = [self.C]


        self.S.prob = {'S':.3,'s':.7}
        self.S.children = [self.C]


        self.C.parents =[self.S, self.P]
        self.C.children = {self.D, self.X}
        self.C.prob = {'pSC': .05, 'psC': .02, 'PSC': .03, 'PsC': .001, 'pSc': .95, 'psc': .98, 'PSc': .97, 'Psc': .999}


        self.X.prob = {'CX': .9, 'cX': .2, 'Cx': .1, 'cx': .8}
        self.X.parents = [self.C]


        self.D.prob = {'CD': .65, 'cD': .3, 'Cd': .35, 'cd': .7}
        self.D.parents = [self.C]

        self.net.addVertex(self.P)
        self.net.addVertex(self.S)
        self.net.addVertex(self.C)
        self.net.addVertex(self.X)
        self.net.addVertex(self.D)
        self.net.addEdge(self.P, self.C)
        self.net.addEdge(self.S, self.C)
        self.net.addEdge(self.C, self.X)
        self.net.addEdge(self.C, self.D)
    def getS(self):
        return self.S
    def getP(self):
        return self.P
    def getC(self):
        return self.C
    def getX(self):
        return self.X
    def getD(self):
        return self.D

    def calcMarginal(self, event):
        #returns P(var) with given CPD tables
        if event == 'P':
            return self.P.prob['P']
        elif event =="p":
            return self.P.prob['p']
        if event == 'S':
            return self.S.prob['S']
        elif event == 's':
            return self.S.prob['s']
        elif event == 'C':
            return (self.C.prob['pSC']* self.calcMarginal('p')* self.calcMarginal('S'))+ \
            (self.C.prob['psC']* self.calcMarginal('p')* self.calcMarginal('s'))+ \
            (self.C.prob['PSC']* self.calcMarginal('P')* self.calcMarginal('S'))+ \
            (self.C.prob['PsC']* self.calcMarginal('P')* self.calcMarginal('s'))
        elif event == 'c':
            return 1 - self.calcMarginal('C')
        elif event == 'X':
            return self.X.prob['CX']* self.calcMarginal('C')+ \
            self.X.prob['cX']* self.calcMarginal('c')
        elif event == 'x':
            return 1 - self.calcMarginal('X')
        elif event == 'D':
            return self.D.prob['CD']* self.calcMarginal('C')+ \
            self.D.prob['cD']* self.calcMarginal('c')
        elif event == 'd':
            return 1 - self.calcMarginal('D')

    def calcJoint(self, eventString):
        #eventString must contain the RV of the Bayes Net in this linearization (P,S,C,X,D)
        #You can omit a RV but never reorder them (eg. PsX is fine. SDX is not)
        #Also eventString must contain 2 RV otherwise just calculate the marginal
        jointProb = 1
        eventArray = list(eventString)
        eventArray.reverse()
        for event in eventArray:
            eventUpper = event.upper()
            #We know that the event is in the bayes net so lets check to see if the event has parents and if those parents are also part of the joint probably calculation
            if self.eventUpper.parents != None:
                for parent in self.eventUpper.parents:
                    if parent in eventArray:
                        #We need to multiply the joint probably by P(event|parent)
                        self.eventUpper.prob[event + parent] *= jointProb

            else:
                #If an event does not have a parent or the parent is not part of the joint that means this event will be independent(or conditionally independent) of the other events
                #so we grab the marginal for the joint
                jointProb *= self.calcMarginal(event)
        return jointProb

class node():
    def __init__(self, name):
        self.prob = {}
        self.parents = None
        self.children = None
        self.probabilities = {}
        self.parents = []


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
            print self.start.get(node)
            print self.start.get(node)

def main():
    test = bayesNetwork()
    print test.calcJoint('SP')



main()



