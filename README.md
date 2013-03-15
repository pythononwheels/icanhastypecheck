#IcanHasTypeCheck (ICHTC)


is a simple python module/library to enable dynamic type checking for python 
method/function calls. Implemented as a decortor. Workinf for python 2.x and 3.x.

Based on annotations for python &gt; 3.x and a naming convention for python &lt; 3.x

it is implemented as a decorator that can be attached to any function or method and will
perform the according (dynamic) typechecking.
It will raise a TypeError if the arguments don't match the function specification.

###Usage is for python 3.x:

```python
	@typecheck
	def foo(param_a: str, param_b: int) -> bool:
		# Do Something 
		return True
```


The base technique for py 3.x are the Function Annotations proposed 
in [PEP 3107](http://www.python.org/dev/peps/pep-3107/). 
They were imlpemented in [Python 3.0](http://docs.python.org/3.0/whatsnew/3.0.html) (see section New Syntax).

All annotated parameter types can be any python expression. 
But for typechecking only types make sense, though.

Since this feature was added from python 3.0 the way I chose for implementing typechecking for
python 2.x is a documentation convention for parameters based on [the info field lists of sphinx](http://sphinx-doc.org/markup/desc.html#info-field-lists). So even when you don't use typechecking you can use it to auto-generate a function documentation.

###Usage for python 2.x:

```python
	@typecheck
	def foo(param_a, param_b):
		""" 
			:type param_a: str
			:type param_b: int
			:rtype: bool	
		 """
		# Do Something 
		return True
```

###Types can be specified as defines in the types module. Like:
```python
	def foo(afunc, param_b):
		""" 
			:type afunc: 	FunctionType
			:type param_b: 	NoneType
			:rtype: 		BooleanType
		"""
		...
```

The decorator typecheck will first check if it is running in a 3.x or 2.x environment and 
react accordingly.


####Alternative Syntax and thoughts:


An alternative to the current way for type declarations could be to use
a simple argument naming_convention: using a type as argument prefix.
This might speed up the matching calculation but has the drawback
of binding the type semantically to the argument name. Will be more effort if
type changes during code evolution. On the other hand gives type info right
where you might need it.  Anyway. I might add this as an option. 

It will look like this: (the docstring is not mandatory, then.)

```python
	@typecheck
	def foo(str_param_a, int_param_b):
		""" 
			Some Docstring ...
		 """
		# Do Something 
		return True
```


### Why is it called IcanHasTypeCheck ?

BTW: The project name "IcanHasTypeCheck" refers to the [famous lolcats](http://en.wikipedia.org/wiki/I_Can_Has_Cheezburger%3F)





