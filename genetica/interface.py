from model.import Genetica
from dna import DNA, genify


class ExampleModel(Genterface):
    def __init__(self):
        #native
        self.a1 = range(1, 10)
        self.a2 = [2,4,5]
        
        #added
        self.fitness = self.logics
        super().connect(self)
        
    def logics(self):
        return self.a1 + self.a1 * self.a2 + self.a2


class Genterface:
    def connect(self, child):
    
        self.child = child
        self.genes_num = len(child.__dict__)
        self.fitness = None
        self.dna = DNA(self.genes_num)
        
        # Convert parameters into genes
        for key, _range in self.child.__dict__:
            self.child.__dict__[key] = genify(_range)
        
    '''def fitness(self):
        """Default fitness function returns better results
        for specie with genes value near to 1
        """
        return sum(self.dna.genes)'''
        