

__author__ = 'Nick'



class bayesNetwork():
    def __init__(self):
        #initialize our network and nodes with probabilities
        self.net ={ \
        'P':{'P':.9,'p':.1,'children':'C'},\

        'S' : {'S':.3,'s':.7, 'children':'C'},\

        'C': {'pSC': .05, 'psC': .02, 'PSC': .03, 'PsC': .001, 'pSc': .95, 'psc': .98, 'PSc': .97, 'Psc': .999,  'parents':['P','p', 'S', 's'], 'children':['X','D']},\

        'X': {'CX': .9, 'cX': .2, 'Cx': .1, 'cx': .8, 'parents':['C','c']},\

        'D': {'CD': .65, 'cD': .3, 'Cd': .35, 'cd': .7, 'parents':['C','c']}}

    def calcMarginal(self, event):
        #returns P(var) with given CPD tables
        if event == 'P':
            return self.net['P']['P']
        elif event =="p":
            return self.net['P']['p']
        if event == 'S':
            return self.net['S']['S']
        elif event == 's':
            return self.net['S']['s']
        elif event == 'C':
            return (self.net['C']['pSC']* self.calcMarginal('p') * self.calcMarginal('S')) + \
            (self.net['C']['psC'] * self.calcMarginal('p') * self.calcMarginal('s')) + \
            (self.net['C']['PSC'] * self.calcMarginal('P') * self.calcMarginal('S')) + \
            (self.net['C']['PsC'] * self.calcMarginal('P') * self.calcMarginal('s'))
        elif event == 'c':
            return 1 - self.calcMarginal('C')
        elif event == 'X':
            return self.net['X']['CX'] * self.calcMarginal('C') + \
            self.net['X']['cX'] * self.calcMarginal('c')
        elif event == 'x':
            return 1 - self.calcMarginal('X')
        elif event == 'D':
            return self.net['D']['CD']* self.calcMarginal('C') + \
            self.net['D']['cD'] * self.calcMarginal('c')
        elif event == 'd':
            return 1 - self.calcMarginal('D')
'''
    def calcJoint(self, eventString):
        #eventString must contain the RV of the Bayes Net in this linearization (P,S,C,X,D)
        #You can omit a RV but never reorder them (eg. PsX is fine. SDX is not)
        #Also eventString must contain 2 RV otherwise just calculate the marginal
        jointProb = 1
        tempProb = 0
        temp = ''

        eventArray = list(eventString)
        reverseArray = eventArray.reverse()
        for event in reverseArray:
            eventUpper = event.upper()
            #We know that the event is in the bayes net so lets check to see if the event has parents and if those parents are also part of the joint probably calculation
            if self.net[eventUpper] == 'C':
                for parent in self.net['C']['parents']:
                    if parent in eventArray:
                        temp += parent
                        tempProb *= self.net[parent.upper()][parent]

                if len(temp) == 2:
                    temp += event
                    jointProb *= self.net['C'][temp] * tempProb
                elif len(temp == 1):
                    if temp == 'S':
                        jointProb *= (self.net['P']['p'] * self.net['S']['S'] * self.net['C']['pSC'] + self.net['P']['P'] * self.net['S']['S'] * self.net['C']['PSC'])
                    elif temp =='s':
                        jointProb *= (self.net['P']['p'] * self.net['S']['s'] * self.net['C']['psC'] + self.net['P']['P'] * self.net['S']['s'] * self.net['C']['PsC'])
                    elif temp =='p':
                        jointProb *= (self.net['P']['p'] * self.net['S']['S'] * self.net['C']['pSC'] + self.net['P']['p'] * self.net['S']['s'] * self.net['C']['psC'])
                    elif temp =='P':
                        jointProb *= (self.net['P']['p'] * self.net['S']['S'] * self.net['C']['PSC'] + self.net['P']['P'] * self.net['S']['s'] * self.net['C']['PsC'])
                else:
                    jointProb *= self.calcMarginal(event)

            elif self.net[eventUpper] == 'D':
                for parent in self.net['D']['parents']:
                    if parent in eventArray:
                        jointProb *= self.net['D'][parent+event]
                    else:
                        jointProb *= self.calcMarginal(event)
            elif self.net[eventUpper] == 'X':
                for parent in self.net['X']['parents']:
                    if parent in eventArray:
                        jointProb *= self.net['X'][parent+event]
                    else:
                        jointProb *= self.calcMarginal(event)
            else:
                jointProb *= self.calcMarginal(event)

    def test(self):
        array = list('PSC')
        temp = ''
        print array
        print self.net['C']['parents']
        for char in array:
            if char in self.net['C']['parents']:
                temp += char
'''


def main():
    test = bayesNetwork()
    print test.calcMarginal('D')
    print test.test()



main()



