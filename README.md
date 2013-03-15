icanhastype
===========

a simple module to enable dynamic type checking for python method/function calls. 
Implemented as a decortor. Workinf for python 2.x and 3.x.

Based on annotations for python &gt; 3.x and a naming convention for python &lt; 3.x

IcanHasType is a simple decorator that can be attached to any function or method and will
perform the according (dynamic) typecheck.
It will raise a TypeError if the arguments don't match the function specification.

Usage is for python 3.x:
```python
	@typecheck
	def foo( param_a: str, param_b: int) -> bool:
		# Do Something 
		return True
```


Base are the Function Annotations proposed in [PEP 3107](http://www.python.org/dev/peps/pep-3107/).
They were imlpemented in [Python 3.0](http://docs.python.org/3.0/whatsnew/3.0.html) (see section New Syntax).

All annotated parameter types can be any python expression. 
But for typechecking only types make sense, though.

Since this feature was added from python 3.0 the way I chose for implementing typechecking for
python 2.x is a naming convention for parameters.

So for python 2.x the Syntax is:
```python
	@typecheck
	def foo( str_param_a, int_param_b):
		# retval: bool
		# Do Something 
		return True
```


The decorator typecheck will first check if it is running in a 3.x or 2.x environment and 
react accordingly.





