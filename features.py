# -*- coding: utf-8 -*-

# Project: TEXTIFY
# ---------------------------------------------------------
# Purpose: Crawling Turkish Language Society's web page
# (tdk.gov.tr) to get Turkish words and their meanings to 
# provide a better service to people who want to contribute
# improvement of Turkish language studies.
# ---------------------------------------------------------
__author__ = "Burak Tekin"
__copyright__ = "Copyleft 2017, Project Textify"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "tknbrk@gmail.com"
__status__ = "Staging"
__credits__ = [
	{
		'contributor': '',
		'contribution': ''
	}
]

import string
import re

from dateutil.parser import parse

class Features():

	def __init__(self):
		self.unique_features = list()
		self.unique_features.append("PUCT")
		self.unique_features.append("VERBATIM")
		self.unique_features.append("DIGIT")
		self.unique_features.append("UNIT")
		self.unique_features.append("DATE")
		self.unique_features.append("UPPER")
		self.unique_features.append("LETTER")
		self.features_of_token = list()

	def token_itself(self, token):
		self.unique_features.append(token)
		self.features_of_token.append(token)

	def is_punctuation(self, token):
		if(token.get_text() in string.punctuation):
			if(token.get_text() == "&" || token.get_text() == "#"):
				self.features_of_token.append("VERBATIM")
			else:
				self.features_of_token.append("PUNCT")

	def is_digit(self, token):
		if(token.get_text().isdigit()):
			self.features_of_token.append("DIGIT")

	def is_unit(self, token):
		regex = re.compile(r'(\d+) ([a-z]{2})')
		unit = regex.match(token.get_text())
		if(unit):
			self.features_of_token.append("UNIT")

	def is_date(self, token):
		if(parse(token.get_text())):
			self.features_of_token.append("DATE")

	def is_all_caps(self, token):
		if(token.get_text() == token.upper()):
			self.features_of_token.append("UPPER")

	def is_letters(self, token):
		regex = re.compile(r'([A-Z]{2})')
		if(token.get_text() == token.upper()):
			self.features_of_token.append("LETTER")

	def feature_extraction(self, token):
		self.token_itself(token)
		self.is_punctuation(token)
		self.is_digit(token)
		self.is_unit(token)
		self.is_date(token)
		self.is_all_caps(token)
		self.is_letters(token)

		return self.features_of_token



