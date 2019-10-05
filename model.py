# -*- coding: utf-8 -*-
"""model module

	All of the genetic algorithm logic happens here.
"""


from dna import DNA
import matplotlib.pyplot as plt
import random


class Genetica:
	def __init__(self, phenotype, genes_num, population_size, fitness_function, mutation_prob=0.03):
		# Class for optimization
		self.phenotype = phenotype

		# Population size
		self.population_size = population_size

		# Optimization function
		self.fitness_function = fitness_function

		# Probability of mutation during crossbreeding
		self.mutation_prob = mutation_prob

		# Population of phenotype instances with randomized gene code
		self.population = [phenotype(DNA(genes_num)) for x in range(population_size)]

		# The history of population's best score for every epoch
		self.history = None

	def run(self, epochs=100):
		"""
		Starts the process of optimization
		:param epochs: Number of iterations
		"""

		# Resetting history
		self.history = list()

		for epoch in range(epochs):
			self.selection()
			self.reproduce()
			self.history.append(self.get_best_fit())

	def plot(self):
		"""
		Show the history plot
		"""

		plt.plot(self.history)
		plt.show()

	def sort_population(self):
		"""
		Sorting population using optimization function
		:return: Sorted population list
		"""
		return sorted(reversed(self.population), key=lambda specie: self.fitness_function(specie))

	def reproduce(self):
		"""
		Update population with new species created from genes of the best ones
		"""

		# Get genes of even (x) and odd (y) species
		genes_x = [self.population[i].dna.genes for i in range(0, len(self.population), 2)]
		genes_y = [self.population[i].dna.genes for i in range(1, len(self.population) - 1, 2)]

		# Take a pair of odd and even species and cross their genes to create a new specie. Add it to the population
		for x in genes_x:
			# Choose random odd specie
			y = random.choice(genes_y)

			# Get new set of genes
			child_dna = self.cross_genes(x, y)

			# Add newly created species to the population
			self.population.append(self.phenotype(child_dna))

	def selection(self):
		"""
		Select 
		:return:
		"""
		self.population = self.sort_population()[:round(self.population_size / 2)]
		return self.population

	def cross_genes(self, genes_x, genes_y):
		child_dna = DNA(0)
		for i in range(len(genes_x)):
			if random.uniform(0, 1) <= 0.5:
				child_dna.genes.append(genes_x[i])
			else:
				child_dna.genes.append(genes_y[i])

		child_dna.mutate(self.mutation_prob)
		return child_dna

	def get_best_fit(self):
		return self.fitness_function(self.sort_population()[0])

	def get_best_specie(self):
		return self.sort_population()[0]

	def get_worst_specie(self):
		return self.sort_population()[-1]



