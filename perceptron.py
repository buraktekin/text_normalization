# -*- coding: utf-8 -*-

# Project: TEXTIFY
# ---------------------------------------------------------
# Purpose: Crawling Turkish Language Society's web page
# (tdk.gov.tr) to get Turkish words and their meanings to 
# provide a better service to people who want to contribute
# improvement of Turkish language studies.
# ---------------------------------------------------------
__author__ = "Burak Tekin"
__copyright__ = "Copyright © 2017, Project Textify"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "tknbrk@gmail.com"
__status__ = "Staging"
__credits__ = []


class Perceptron():

	def __init__(self):
		self.name = ""
		self.weights = dict()

	def prediction_score(self, token):
		sum = 0.0
		for feature in token.feature_extraction():
			if(feature not in self.weights):
				self.weights[feature] = 0.0
			else:
				sum += self.weights[feature]

		return sum

	def set_name(self, classname):
		self.name = classname

	def get_name(self):
		return self.name

# public double predictionScore(Token token) {
# 	double sum = 0;
# 	for(String feature : token.featureExtraction()) {
# 		if(!getClassWeights().containsKey(feature)) {
# 			getClassWeights().putIfAbsent(feature, Helpers.formatRandomValues(Helpers.randomWeightGenerator(-5, 5)));
# 		}
# 		sum += getClassWeights().get(feature);
# 	}
# 	return sum;
# }