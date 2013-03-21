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

ALL_PARAM_TYPES_PATTERN = r":type[\s]+(\w+):[\s]+([\w\.]+)"
ALL_RETURN_TYPES_PATTERN = r":rtype:[\s]+([\w\.]+)"

def print_list(name, alist):
	""" just printing a parameter list in a readable way
		:type name: 	types.StringType
		:type alist: 	types.ListType
	"""
	print "%s" % (name)
	print "--------------------"
	for elem in alist:
		print elem
	print

def print_func_spec(func):
	""" print a function specification including 
		function arguments and type specs.
		:type func: types.FunctionType
	"""

	spec = inspect.getargspec(func)
	doc = inspect.getdoc(func)
	print "Printing specification for function: %s" % (str(func))
	print "-"*70
	print "getargspec: %s" % (str(spec))
	print "Parameter Type spec in docstring: %s" % (doc)
	
	types = re.compile(ALL_PARAM_TYPES_PATTERN, re.IGNORECASE)	
	rtypes = re.compile(ALL_RETURN_TYPES_PATTERN, re.IGNORECASE)	
	res = types.findall(doc)
	print_list("Listing parameter types", res)
	res = rtypes.findall(doc)
	print_list("return type", res)

	
def get_class_type(kls):
	"""
		get and return the type of a class 
		:type kls: types.StringType
	"""
	#print "get_class_type for %s" % (kls)
	if kls.count(".") > 0:
		#kls_instance = reduce(getattr, str.split("."), sys.modules[__name__])
		#print "partitioned: ", kls.rpartition(".")
		module = kls.rpartition(".")[0]
		mod = __import__(module, globals(), locals(), [], -1)
		klass = kls.rpartition(".")[2]
		#print module, mod, klass
		kls_instance = getattr(mod, klass)
	else:
		#print dir(sys.modules[__name__])
		#print sys.modules[__name__]
		kls_instance = getattr(sys.modules[__name__], kls)
	#print kls_instance
	#print type(kls_instance)
	return kls_instance

def typesafe(parameter_spec = None):
	def typecheck(func):
		""" Decorator to verify function argument types 
			inspired and partly take from the book:
			Pro Python. (Expert's Voice in Open Source)
			From Marty Alchin 
			(see)[http://www.amazon.de/Python-Experts-Voice-Open-Source/dp/1430227575]

			:type func: types.FunctionType
			
			:rtype: types.FunctionType
		"""

		#print "-"*70
		#print "Checking Type Safety for function: %s" % (str(func))
		#print "-"*70

		error = "Wrong type for %s: expected: %s, got %s."
		fine = "Right type for %s: expected: %s, and successfully got %s."

		if sys.version_info[0] == 3:
			##########################
			# Handle python > 3.x
			##########################
			#spec = inspect.getfullargspec(func)
			#doc = inspect.getdoc(func)
			#annotations = spec.annotations
			@functools.wraps(func)
			def wrapper(*args, **kwargs):
				# Not implemented for python 3.x, yet
				return func
				# handle keyword args
				#for name, arg in chain(zip(spec.args,args), kwargs.items()):
				#	if name in annotations and not isinstance(arg, annotations[name]):
				#		raise TypeError( error % ( name, 
				#								   annotations[name].__name__, 
				#								   type(arg).__name__ ) )
				#return func
			return wrapper
		else:
			############################
			# Handle python < 3.x
			############################
			spec = inspect.getargspec(func)
			doc = inspect.getdoc(func)
			type_dict = {}

			if parameter_spec:
				# the parameter specification is passed as a paramter to the decorator
				all_types = parameter_spec.items()
			else:
				# the parameter spec is defined as docstring.
				# Regexps for the func specs
				all_param_types = re.compile(ALL_PARAM_TYPES_PATTERN, re.IGNORECASE)	
				all_rtypes = re.compile(ALL_RETURN_TYPES_PATTERN, re.IGNORECASE)	
				all_types = all_param_types.findall(doc)	
			#print "all_types:", all_types
			for name, atype in all_types:
				#print "trying to get Type %s for: %s" % (name, atype)
				obj = get_class_type(atype)
				#print "got: %s" % (obj)
				type_dict[name] = obj
			#print type_dict
			
			@functools.wraps(func)
			def wrapper(*args, **kwargs):
				# handle keyword args
				for name, arg in chain(zip(spec.args,args), kwargs.items()):
					if name in type_dict and not isinstance(arg, type_dict[name]):
						raise TypeError( error % ( name, 
												   type_dict[name], 
												   type(arg).__name__ ) )
					else:
						#print fine %  ( name, type_dict[name], type(arg).__name__ ) 
						pass
				return func
			return wrapper
	return typecheck
			


if __name__ == "__main__":
	print "not intended to be used on the cli ;)"
	print "usage: see: https://github.com/pythononwheels/icanhastypecheck "