import random

class DNA:
	def __init__(self, genes_num):
		self.genes = [0.5 for i in range(genes_num)]
		for	i in range(len(self.genes)):
			self.genes[i] = round(random.uniform(0, 1), 2)

	def mutate(self,mutation_prob):
		for	i in range(len(self.genes)):
			if random.uniform(0, 1) > mutation_prob:
				continue

			self.genes[i] = round(random.uniform(0, 1), 2)


def genify(list_, gen):
	prob_step = round(1 / len(list_), 2)

	for i in range(len(list_) - 1):
		if gen <= (i) * prob_step:
			return(list_[i])
	else:
		return(list_[-1])
