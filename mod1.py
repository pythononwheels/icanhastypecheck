#
# exmaple Module for TypeCheck Test
# 
import os

class Point(object):
	
	def __init__(self, x = None, y = None):
		""" Initialize the Point. Can be used to give x,y directly."""
		self.x = x
		self.y = y

	def set_coord(self, x , y):
		self.x = x
		self.y = y		

	def __repr__(self):
		ostr = ""
		ostr = "x: " + str(self.x) + os.linesep
		ostr += "y: " + str(self.y) + os.linesep
		return ostr
	
	def __str__(self):
		return self.__repr__()
		

