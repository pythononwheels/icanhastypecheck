#IcanHasTypeCheck (ICHTC)


is a small and easy to use python module/library to enable dynamic type checking for python 
method and function calls. Implemented as a decorator. Working ans tested for python 2.x .
(Plans and an example implementation for python 3.x is included )

Function type specification is based on a naming/docstring convention for python &lt; 3.x

Typechecking is implemented as a decorator that can be attached to any function or method and will
perform the according (dynamic) typechecking.
It will raise a TypeError if the arguments don't match the function specification.

## Python 2.x
Since function annotations are not available in python 2.x the way I chose to implement typechecking for
python 2.x is a documentation convention for parameters based on [the info field lists of sphinx](http://sphinx-doc.org/markup/desc.html#info-field-lists). So even when you don't use typechecking you can use it to auto-generate a function documentation.
There is an alternative approach for those of you who don't like docstings in sphinx format which úses a naming convention. (See Alternatives below)

###Syntax for python 2.x / docstrings:

```python
	@typesafe
	def foo(param_a, param_b):
		""" 
			:type param_a: 	types.StringType
			:type param_b: 	types.IntType
			:rtype: 		types.BooleanType	
		 """
		# Do Something 
		return True
```

###You can use any type. 

So if you have defined a Point() class in mod1 then  you could specify is like:

class Point(object):
	```python
		# File: mod1.py
   		def __init__(self, x = None, y = None):
			""" Initialize the Point. Can be used to give x,y directly."""
			self.x = x
			self.y = y
	```

```python
	# another module.py
	from mod1 import Point

	def foo(afunc):
		""" 
			:type afunc: 	mod1.Point			
			:rtype: 		types.BooleanType
		"""
		return True
```

The decorator typesafe will first check if it is running in a 3.x or 2.x environment and 
react accordingly.

### Installation and Example:

Just download the zip or tarball. Unpack it and run 
    
    pyhton i_is_example.py



####Alternative Syntax and thoughts:


An alternative to the current way for type declarations could be to use
a simple argument naming_convention: using a type as argument prefix.
This might speed up the matching calculation but has the drawback
of binding the type semantically to the argument name. Will be more effort if
type changes during code evolution. On the other hand gives type info right
where you might need it.  Anyway. I might add this as an option. 

It will look like this: (the docstring is not mandatory, then.)

```python
	@typesafe
	def foo(str_param_a, int_param_b):
		""" 
			Some Docstring ...
		 """
		# Do Something 
		return True
```


## Python 3.x (Just an implementation example -> Not tested)
The base technique for IcanHasTypeCheck in python 3.x are the Function Annotations proposed 
in [PEP 3107](http://www.python.org/dev/peps/pep-3107/). 
They were implemented in [Python 3.0](http://docs.python.org/3.0/whatsnew/3.0.html) (see section New Syntax).

###Syntax for python 3.x:

```python
	@typesafe
	def foo(param_a: str, param_b: int) -> bool:
		# Do Something 
		return True
```
The @typesafe decorator will then check all arguments dynamically whenever the foo is called for valid types.
As a quoting remark from the PEP 3107: "All annotated parameter types can be any python expression. "
But for typechecking only types make sense, though.
The idea and parts of the implementation were inspired by the book: [Pro Python (Expert's Voice in Open Source)](http://www.amazon.de/Python-Experts-Voice-Open-Source/dp/1430227575)

### Why is it called IcanHasTypeCheck ?

BTW: The project name "IcanHasTypeCheck" refers to the [famous lolcats](http://en.wikipedia.org/wiki/I_Can_Has_Cheezburger%3F)





