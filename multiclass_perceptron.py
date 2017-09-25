class MCP(object):
	"""docstring for MCP"""
	def __init__(self):
		self.MAX_ITERATION = 10
		self.perceptrons = dict()

		def create_perceptrons(self, unique_classnames):
			for classname in unique_classnames:
				p = Perceptron()
		