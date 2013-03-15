#
# Example Script for IcanHasType  
# typecheck library for python 
# 


import re, sys
import inspect

def foo( param_a, param_b, param_c=42, param_d="atest"):
		""" 
			:type param_a: str
			:type param_b: int
			:rtype: bool	
		 """
		# Do Something 
		print "foo"
		return True

def print_list(name, l):
	print "%s list" % (name)
	print "--------------------"
	for elem in l:
		print elem
	print

	


if __name__ == "__main__":
	foo(1,2)
	spec = inspect.getargspec(foo)
	doc = inspect.getdoc(foo)
	print spec
	print doc
	
	types = re.compile(r":type[\s]+(\w+):[\s]+(\w+)", re.IGNORECASE)	
	rtypes = re.compile(r":rtype:[\s]+(\w+)", re.IGNORECASE)	
	res = types.findall(doc)
	print_list("type", res)
	res = rtypes.findall(doc)
	print_list("rtype", res)