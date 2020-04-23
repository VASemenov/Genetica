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

### Imports
```python
from model import Genetica
from dna import genify
```

### Class structure

```python
class ExampleModel:
    def __init__(self, dna):
        self.dna = dna

        # Class parameters that are inputs for optimization
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

```

### Running optimization
```python
model = Genetica(ExampleModel, 2, 1000, lambda x: x.result)
model.run()
```


### Getting results
```python
print("BEST FIT:", model.get_best_fit())
print("PARAMS OF BEST FIT:", model.get_best_specie().a1, model.get_best_specie().a2)

# Getting populations history of best results for each epoch
model.plot()
```
