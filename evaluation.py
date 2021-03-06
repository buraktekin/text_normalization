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
		'contributor': 'https://github.com/mertemin',
		'contribution': 'Turkish word list'
	}
]

from corpus import Corpus
from multiclass_perceptron import MCP

c = Corpus()
token_list = c.read_file('en_train.csv')

mcp = MCP()
mcp.create_perceptrons(c)
mcp.train(c, 10)
mcp.test(c)

