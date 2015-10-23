def main():
    omg = bayesNetwork()
    print omg.calcMarginal('d')



class bayesNetwork():
    def __init__(self):
        #initialize our network and nodes with probabilities
        self.diseasePredictor = network()
        self.pollution = node('p')
        self.pollution.probabilities = {'p':.9,'~p':.1}
        self.smoker = node('s')
        self.smoker.probabilities = {'s':.3,'~s':.7}
        self.cancer = node('c')
        self.cancer.parents =[self.smoker, self.pollution]
        self.cancer.probabilities = {'c|~ps': .05, 'c|~p~s': .02, 'c|ps': .03, 'c|p~s': .001, '~c|~ps': .95, '~c|~p~s': .98, '~c|ps': .97, '~c|p~s': .999}
        self.xRay = node('x')
        self.xRay.probabilities = {'x|c': .9, 'x|~c': .2, '~x|c': .1, '~x|~c': .8}
        self.xRay.parents = [self.cancer]
        self.dyspnoea = node('d')
        self.dyspnoea.probabilities = {'d|c': .65, 'd|~c': .3, '~d|c': .35, '~d|~c': .7}
        self.dyspnoea.parents = [self.cancer]
        #create graph network
        self.diseasePredictor.addVertex(self.pollution)
        self.diseasePredictor.addVertex(self.smoker)
        self.diseasePredictor.addVertex(self.cancer)
        self.diseasePredictor.addVertex(self.xRay)
        self.diseasePredictor.addVertex(self.dyspnoea)
        self.diseasePredictor.addEdge(self.pollution, self.cancer)
        self.diseasePredictor.addEdge(self.smoker, self.cancer)
        self.diseasePredictor.addEdge(self.cancer, self.xRay)
        self.diseasePredictor.addEdge(self.cancer, self.dyspnoea)

    def calcMarginal(self, var):
        #returns P(var) with given CPD tables
        if var == 'p':
            return self.pollution.probabilities['p']
        elif var =="~p":
            return self.pollution.probabilities['~p']
        if var == 's':
            return self.smoker.probabilities['s']
        elif var == '~s':
            return self.smoker.probabilities['~s']
        elif var == 'c':
            return (self.cancer.probabilities['c|~ps']* self.calcMarginal('~p')* self.calcMarginal('s'))+ \
            (self.cancer.probabilities['c|~p~s']* self.calcMarginal('~p')* self.calcMarginal('~s'))+ \
            (self.cancer.probabilities['c|ps']* self.calcMarginal('p')* self.calcMarginal('s'))+ \
            (self.cancer.probabilities['c|p~s']* self.calcMarginal('p')* self.calcMarginal('~s'))
        elif var == '~c':
            return 1 - self.calcMarginal('c')
            '''(self.cancer.probabilities['~c|~ps']* self.calcMarginal('~p')* self.calcMarginal('s'))+ \
            (self.cancer.probabilities['~c|~p~s']* self.calcMarginal('~p')* self.calcMarginal('~s'))+ \
            (self.cancer.probabilities['~c|ps']* self.calcMarginal('p')* self.calcMarginal('s'))+ \
            (self.cancer.probabilities['~c|p~s']* self.calcMarginal('p')* self.calcMarginal('~s'))'''
        elif var == 'x':
            return self.xRay.probabilities['x|c']* self.calcMarginal('c')+ \
            self.xRay.probabilities['x|~c']* self.calcMarginal('~c')
        elif var == '~x':
            return 1 - self.calcMarginal('x')
        elif var == 'd':
            return self.dyspnoea.probabilities['d|c']* self.calcMarginal('c')+ \
            self.dyspnoea.probabilities['d|~c']* self.calcMarginal('~c')
        elif var == '~d':
            return 1 - self.calcMarginal('d')

    def calcJoint(self,array):
        #calculates joint probably - assume array is (P,S,C,X,D)
        #no need to calculate with just one RV because that would simply be the marginal
        if array.length == 2: #P(P,S)
            return self.pollution.probabilities[array[0]]* self.smoker.probabilities[array[1]]
        elif array.length == 3:#P(P,S,C)
            if array[0] == 'p' and array[0] == 's':
                if array[2] == 'c':
                    return self.calcJoint(['p','s'])* self.cancer.probabilities['c|ps']
                else:
                    return self.calcJoint(['p','s'])* self.cancer.probabilities['~c|ps']
            elif array[0] == '~p' and array[0] == 's':
                if array[2] == 'c':
                    return self.calcJoint(['~p','s'])* self.cancer.probabilities['c|~ps']
                else:
                    return self.calcJoint(['~p','s'])* self.cancer.probabilities['~c|~ps']
            elif array[0] == 'p' and array[0] == '~s':
                if array[2] == 'c':
                    return self.calcJoint(['p','~s'])* self.cancer.probabilities['c|p~s']
                else:
                    return self.calcJoint(['p','~s'])* self.cancer.probabilities['~c|p~s']
            elif array[0] == '~p' and array[0] == '~s':
                if array[2] == 'c':
                    return self.calcJoint(['~p','~s'])* self.cancer.probabilities['c|~p~s']
                else:
                    return self.calcJoint(['~p','~s'])* self.cancer.probabilities['~c|~p~s']
        elif array.length == 4:#P(P,S,C,X) or P(P,S,C,D):
            if array[0] == 'p' and array[1]=='s' and array[2] == 'c':

                return self.calcJoint(['p','s','c'])*self.xRay.probabilites['x|c']
            else:
                return self.calcJoint(['p','s','s'])* self.xRay.probabilities['~x|c']





    def calcJoint(self,a,b):
        #calculate a|b
        if b == 'd' or b == '~d' or b == 'x' or b =='~b':
            return diagnostic(self,a,b)

        #I know how to calculate these but its getting too late - Also know how to do conditionals but it would take  too long
        

    def diagnostic(self,a,b):















class node():
    def __init__(self, name):
        self.probabilities = {}
        self.parents = []
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
            print self.start.get(node)










main()