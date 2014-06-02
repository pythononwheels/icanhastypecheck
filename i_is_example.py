#
# Example Script for IcanHasType  
# typecheck library for python 
# 


import re, sys
import inspect
from typecheck import typesafe
import mod1 
import typecheck

@typesafe()
def foo( param_a, param_b):
		""" 
			:type param_a: 	types.IntType
			:type param_b: 	types.StringType
			:rtype: 		types.BooleanType	
		 """
		# Do Something 
		print "foo"
		return True


#{ "param_a" : "mod1.Point"}
@typesafe({ "param_a": str })
def bar( param_a ):
	"""
		:type param_a: mod1.Point
	"""	
	print "Yeah, I was called"


@typesafe({ "val" : mod1.Point })
def point_check( val ):
	""" gets a point and prints it """
	print " ** Printing a mod1.Point "
	print val
	return

if __name__ == "__main__":
	# passes successfully (see function  spec above)
	# foo uses the sphinx documentation style to specify the
	# function parameter types
	foo(1, "test")
	
	# calls bar function which uses the decorator parmaters
	# to specify the function parameter types
	bar("test")
	
	# this will (pretty)print a function specification
	typecheck.print_func_spec(foo)
	
	# uses a user defined class (mod1.Point, see mod1.py) 
	# as the specified/required type for function point_check
	p = mod1.Point()
	p.x = 11
	p.y = 4
	point_check(p)

	# the following call of foo will fail (successfuly) 
	# with a TypeError because it passes an int as second 
	# parameter instead of the specified str
	#foo(1,2)

	


