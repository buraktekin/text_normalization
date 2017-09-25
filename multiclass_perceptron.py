from features import Features
from perceptron import Perceptron

class MCP(object):
	"""docstring for MCP"""
	def __init__(self):
		self.MAX_ITERATION = 10
		self.perceptrons = dict()

	def create_perceptrons(self, corpus):
		for classname in corpus.get_list_of_unique_classnames():
			p = Perceptron()
			p.set_name = classname
			for feature in Features().get_unique_features():
				if(feature not in p.weights):
					p.weights[feature] = 0.0

			if(p not in self.perceptrons):
				self.perceptrons[classname] = p

		return self.perceptrons
	
	def predict(self, token):
		winner_perceptron = self.perceptrons['PLAIN']
		previous_score = winner_perceptron.prediction_score(token);
		score_check = 0.0

		for perceptron in self.perceptrons:
			score = self.perceptrons[perceptron].prediction_score(token)
			if(score > previous_score):
				winner_perceptron = perceptron

		return winner_perceptron

	def train(self, corpus, MAX_ITERATION):
		iteration = 0
		while(iteration < self.MAX_ITERATION):
			counter = 0
			error_counter = 0
			for token in corpus.get_list_of_tokens():
				counter += 1
				winner = self.predict(token)
				gold = self.perceptrons[token.get_class()]

				if(winner.get_name() != gold.get_name()):
					error_counter += 1
					for feature in token.feature_extraction():
						value_gold = gold.weights[feature]
						value_winner = winner.weights[feature]
						value_gold += 1
						value_winner -= 1
						gold.weights[feature] = value_gold
						winner.weights[feature] = value_winner

			ratioOfWrongPredictions = errorCounter * 100 / counter
			line = "Misclassified tokens encountered @ batch-{}".format(str(iteration) + ": " + str(errorCounter) + "/" + str(counter) + " => " + str(ratioOfWrongPredictions) + "%")
			print line
			iteration += 1


	def test(self, corpus):
		iteration = 0
		counter = 0
		errorCounter = 0
		for token in corpus.get_list_of_unique_classnames():
			counter += 1
			token_gold = token.get_class()
			token.set_class(self.predict(token).get_class())
			if(token_gold != token.get_class()):
				errorCounter += 1

		ratioOfWrongPredictions = errorCounter * 100 / counter
		line = "Misclassified tokens encountered @ batch-{}".format(str(iteration) + ": " + str(errorCounter) + "/" + str(counter) + " => " + str(ratioOfWrongPredictions) + "%")
		print line
		iteration += 1
