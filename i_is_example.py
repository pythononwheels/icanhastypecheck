#
# Example Script for IcanHasType  
# typecheck library for python 
# 


import re, sys
import inspect
from typecheck import typesafe
from mod1 import Point
import typecheck

@typesafe
def foo( param_a, param_b):
		""" 
			:type param_a: types.IntType
			:type param_b: types.StringType
			:rtype: BooleanType	
		 """
		# Do Something 
		print "foo"
		return True



@typesafe
def mod_test( param_a ):
	"""
		:type param_a: mod1.Point
	"""	
	print "Yeah, I was called"


if __name__ == "__main__":
	# passes successfully (see function  spec above)
	foo(1, "test2")
	# fails 'successfully' (see function  spec above)
	#foo(1, 2)
	p = Point()
	mod_test(p)
	typecheck.print_func_spec(mod_test)

	


