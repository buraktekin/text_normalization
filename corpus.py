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

import os
import codecs

from itertools import islice
from definitions import ROOT_DIR
from token import Token

class Corpus():

	def __init__(self):
		self.list_of_tokens = list()
		self.list_of_unique_classnames = list()


	def read_file(self, file):
		with codecs.open(ROOT_DIR + '/dataset/' + file, 'r') as document:
			lines = document.readlines()
			for line in islice(lines, 1, len(lines)):
				partials = line.split(",")
				token = self.create_token(partials)
				self.list_of_tokens.append(token.__dict__)

		return self.list_of_tokens


	def create_token(self, object):
		token = Token()
		token.set_token(object)
		self.find_unique_classnames(token)
		return token


	def find_unique_classnames(self, token):
		classname = token.class_type
		if(classname not in self.list_of_unique_classnames):
			self.list_of_unique_classnames.append(classname)
		else:
			pass


c = Corpus()
print c.read_file('en_train.csv')
print c.list_of_unique_classnames