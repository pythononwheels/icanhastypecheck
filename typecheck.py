#
# Module containing the main typecheck decorator.
# Author: khz
# Date: 03 / 2013
# Hosted on Github:  https://github.com/pythononwheels/icanhastype
# 
import inspect
import functools
import re
from itertools import chain

def typesafe(func):
	""" Decorator to verify function argument types 
		inspired and partly take from the book:
		Pro Python. (Expert's Voice in Open Source)
		From Marty Alchin 
		(see)[http://www.amazon.de/Python-Experts-Voice-Open-Source/dp/1430227575]
	"""
	
	

	error = "Wrong type for %s: expected: %s, got %s."

	if sys.version_info[0] == 3:
		# Handle python > 3.x
		spec = inspect.getfullargspec(func)
		doc = inspect.getdoc(func)
		annotations = spec.annotations
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			# handle keyword args
			for name, arg in chain(zip(spec.args,args), kwargs.items()):
				if name in annotations and not instance(arg, annotations[name]):
					raise TypeError( error % ( name, 
											   annotations[name].__name__, 
											   type(arg).__name__ ) )
			return func
		return wrapper
	else:
		# Handle python < 3.x
		spec = inspect.getargspec(func)
		doc = inspect.getdoc(func)
		# handle keyword args

		# Regexps for the fucn specs
		#:type param_a: str
		#:type param_b: int
		#:rtype: bool	
		pat1 = re.compile(r":type\s[a-zA-Z]+[a-zA-Z0-9]*:\s[a-zA-Z]+")
		pat1.match(doc)
		print pat1
			

	




if __name__ == "__main__":
	print "not intended to be used on the cli ;)"
