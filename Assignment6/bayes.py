from Assignment6.graph import node
from Assignment6.graph import network

__author__ = 'Nick'



class bayesNetwork():
    def __init__(self):
        #initialize our network and nodes with probabilities

        self.pollution = node('P')
        self.pollution.prob = {'P':.9,'p':.1}
        self.pollution.children = [self.cancer]

        self.smoker = node('S')
        self.smoker.prob = {'S':.3,'s':.7}
        self.smoker.children = [self.cancer]

        self.cancer = node('C')
        self.cancer.parents =[self.smoker, self.pollution]
        self.cancer.children = {self.dyspnoea, self.xRay}
        self.cancer.prob = {'pSC': .05, 'psC': .02, 'PSC': .03, 'PsC': .001, 'pSc': .95, 'psc': .98, 'PSc': .97, 'Psc': .999}

        self.xRay = node('X')
        self.xRay.prob = {'CX': .9, 'cX': .2, 'Cx': .1, 'cx': .8}
        self.xRay.parents = [self.cancer]

        self.dyspnoea = node('D')
        self.dyspnoea.prob = {'CD': .65, 'cD': .3, 'Cd': .35, 'cd': .7}
        self.dyspnoea.parents = [self.cancer]

    def calcMarginal(self, event):
        #returns P(var) with given CPD tables
        if event == 'P':
            return self.pollution.prob['P']
        elif event =="p":
            return self.pollution.prob['p']
        if event == 'S':
            return self.smoker.prob['S']
        elif event == 's':
            return self.smoker.prob['s']
        elif event == 'C':
            return (self.cancer.prob['pSC']* self.calcMarginal('p')* self.calcMarginal('S'))+ \
            (self.cancer.prob['psC']* self.calcMarginal('p')* self.calcMarginal('s'))+ \
            (self.cancer.prob['PSC']* self.calcMarginal('P')* self.calcMarginal('S'))+ \
            (self.cancer.prob['PsC']* self.calcMarginal('P')* self.calcMarginal('s'))
        elif event == 'c':
            return 1 - self.calcMarginal('C')
        elif event == 'X':
            return self.xRay.prob['CX']* self.calcMarginal('C')+ \
            self.xRay.prob['cX']* self.calcMarginal('c')
        elif event == 'x':
            return 1 - self.calcMarginal('X')
        elif event == 'D':
            return self.dyspnoea.prob['CD']* self.calcMarginal('C')+ \
            self.dyspnoea.prob['cD']* self.calcMarginal('c')
        elif event == 'd':
            return 1 - self.calcMarginal('D')

    def calcJoint(self, eventString):
        #eventString must contain the RV of the Bayes Net in this linearization (P,S,C,X,D)
        #You can omit a RV but never reorder them (eg. PSX is fine. SDX is not)
        #Also eventString must contain 2 RV otherwise just calculate the marginal
        jointProb = 1
        eventArray = list(eventString)
        eventArray.reverse()
        for event in eventArray:
            event.upper()







