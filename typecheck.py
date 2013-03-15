#
# Module containing the main typecheck decorator.
# Author: khz
# Date: 03 / 2013
# Hosted on Github:  https://github.com/pythononwheels/icanhastype
# 
import inspect
import functools
import re
import sys
from itertools import chain
import types

def typesafe(func):
	""" Decorator to verify function argument types 
		inspired and partly take from the book:
		Pro Python. (Expert's Voice in Open Source)
		From Marty Alchin 
		(see)[http://www.amazon.de/Python-Experts-Voice-Open-Source/dp/1430227575]

		:type func: types.FunctionType
		
		:rtype: type.NoneType
	"""
	
	

	error = "Wrong type for %s: expected: %s, got %s."
	fine = "Right type for %s: expected: %s, and successfully got %s."

	if sys.version_info[0] == 3:
		# Handle python > 3.x
		spec = inspect.getfullargspec(func)
		doc = inspect.getdoc(func)
		annotations = spec.annotations
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			# handle keyword args
			for name, arg in chain(zip(spec.args,args), kwargs.items()):
				if name in annotations and not isinstance(arg, annotations[name]):
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
		all_param_types = re.compile(r":type[\s]+(\w+):[\s]+(\w+)", re.IGNORECASE)	
		all_rtypes = re.compile(r":rtype:[\s]+(\w+)", re.IGNORECASE)	
		all_types = all_param_types.findall(doc)
		type_dict = {}
		for name, atype in all_types:
			type_dict[name] = atype
		print type_dict
		
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			# handle keyword args
			for name, arg in chain(zip(spec.args,args), kwargs.items()):
				if name in type_dict and not isinstance(arg, getattr(types, type_dict[name])):
					raise TypeError( error % ( name, 
											   type_dict[name], 
											   type(arg).__name__ ) )
				else:
					print fine %  ( name, 
									type_dict[name], 
									type(arg).__name__ ) 
			return func
		return wrapper
			

	




if __name__ == "__main__":
	print "not intended to be used on the cli ;)"
