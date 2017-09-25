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

from features import Features

class Token(object):
	"""docstring for Token"""
	def __init__(self):
		self.sentence_id = ""
		self.token_id = ""
		self.class_type = ""
		self.before = ""
		self.after = ""

	def get_text(self):
		return self.before

	def set_text(self, text):
		self.before = text

	def get_prediction(self):
		return self.after

	def set_prediction(self, prediction):
		self.after = prediction

	def get_class(self):
		return self.class_type

	def set_class(self, classname):
		self.class_type = classname

	def set_token(self, object):
		self.sentence_id = object[0]
		self.token_id = object[1]
		self.class_type = object[2].replace('"', '', 2)
		self.before = object[3].replace('"', '', 2)
		self.after = object[4].replace('"', '', 2)

	def feature_extraction(self):
		f = Features()
		feature_of_token = f.feature_extraction(self)
		print feature_of_token
		return feature_of_token
