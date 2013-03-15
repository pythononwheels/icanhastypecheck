#
# Example Script for IcanHasType  
# typecheck library for python 
# 


import re, sys
import inspect
from typecheck import typesafe

@typesafe
def foo( param_a, param_b):
		""" 
			:type param_a: IntType
			:type param_b: StringType
			:rtype: BooleanType	
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
	foo(1, "test2")
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

	rtypes = rtypes.findall(doc)


