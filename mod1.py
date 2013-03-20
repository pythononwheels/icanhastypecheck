#
# exmaple Module for TypeCheck Test
# 

class Point(object):
	
	def __init__(self, x = None, y = None):
		""" Initialize the Point. Can be used to give x,y directly."""
		self.x = x
		self.y = y

	def set_coord(self, x , y):
		self.x = x
		self.y = y		

		
