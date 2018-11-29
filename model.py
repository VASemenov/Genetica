from dna import DNA, genify
import matplotlib.pyplot as plt
import math
import random


class Genetica:
	def __init__(self, phenotype, genes_num, population_size, fitness_function, mutation_prob=0.03):
		self.phenotype = phenotype
		self.population_size = population_size
		self.fitness_function = fitness_function
		self.mutation_prob = mutation_prob
		self.population = [phenotype(DNA(genes_num)) for x in range(population_size)]
		self.history = list()

	def run(self, epochs = 100):
		self.history = list()
		for epoch in range(epochs):
			self.selection()
			self.reproduce()
			self.history.append(self.get_best_fit())

	def plot(self):
		plt.plot(self.history)
		plt.show()

	def sort_population(self):
		return sorted(reversed(self.population), key=lambda specie: self.fitness_function(specie))

	def reproduce(self):
		genes_x = [self.population[i].dna.genes for i in range(0, len(self.population), 2)]
		genes_y = [self.population[i].dna.genes for i in range(1, len(self.population) - 1, 2)]
		children = list()

		for x in genes_x:
			y = random.choice(genes_y)
			child_dna = self.cross_genes(x, y)
			self.population.append(self.phenotype(child_dna))

	def selection(self):
		self.population = self.sort_population()[:round(self.population_size / 2)]
		return self.population

	def get_best_fit(self):
		return self.fitness_function(self.sort_population()[0])

	def get_best_specie(self):
		return self.sort_population()[0]

	def cross_genes(self, genes_x, genes_y):
		child_dna = DNA(0)
		for i in range(len(genes_x)):
			if random.uniform(0, 1) <= 0.5:
				child_dna.genes.append(genes_x[i])
			else:
				child_dna.genes.append(genes_y[i])

		child_dna.mutate(self.mutation_prob)
		return child_dna



