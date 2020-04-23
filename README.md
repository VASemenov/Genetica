# Genetica

## About

**Genetica** is the minimalistic genetic algorithm library for optimizing class parameters.

This library allows you to take any class with certain business logic, modify it a little and then give it back to Genetica to optimize.

Right now Genetica is a *minimalistic* library. It lacks some of the fancy aspects of genetic algorithms. Nevertheless, the library was created to optimize some aerospace designs for the author's graduation project.

Now you can enjoy the core idea of genetic optimization without much pain of getting into it:

- Turning class parameters into manipulatable genes
- Population generation (any size)
- Crossbreeding with mutations
- Learning process chart (not real-time)
- Real-time learning feedback
- Getting the best and worst species' parameters

## Installation

Genetica is supported by Pyhton 3.x

Install it through pip:
    
    pip install genetica

## Quick start

'''python

from model import Genetica
from dna import genify

# EXAMPLE
# This is how a target class should be structured

class ExampleModel:
    def __init__(self, dna):
        self.dna = dna

        # Class paraters that are inputs for optimization
        self.a1 = genify(range(1,1890), dna.genes[0])
        self.a2 = genify(range(1,2017), dna.genes[1])

        #                 | enum of         | just get a
        #                    possible        certain gen
        #                        params |    to randomize 
        #                 |             |    this parameter|   
        #                 |             |   |              |
        #self.a2 = genify( range(1,2017),      dna.genes[1] )

        # Target parameter to optimize
        self.result = self.fitness()
        
    def fitness(self):
        return self.a1 ** self.a1 + self.a1 * self.a2 + self.a2


# EXAMPLE
# Finding min of parameter result in ExampleModel
# Genetica gets class, number of needed genes to genify parameters, and lambda function, that is,
# essentially a fitness function

model = Genetica(ExampleModel, 2, 1000, lambda x: x.result)
model.run()

print("BEST FIT:", model.get_best_fit())
print("PARAMS OF BEST FIT:", model.get_best_specie().a1, model.get_best_specie().a2)

# Getting populations history of best results for each epoch
model.plot()

'''
