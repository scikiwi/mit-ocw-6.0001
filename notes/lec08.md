# Object Oriented Programming
Python allows many kinds of data, eg lists, `int`s, `float`s, strings, and dictionaries.
Each is an **object**. Every object has:
* a type
* an internal data representation (primitive or composite)
* a set of procedures for interaction with the object
***
An object is an **instance** of a type. For example:
* `1234` is an instance of an `int`
* `"hello"` is an instance of a string
***
Objects are a data abstraction that captures:
* an internal representation (through data attributes)
* an interface for interacting with the object (through procedural attributes)
***
What are attributes?
* **Attributes** are data and procedures that "belong" to a class
* Think of **data attributes** as *other* objects that make up a class (eg, a coordinate is made up of two `float`s)
* Think of **procedural attributes** (aka methods) as functions to interact with an object that work only with this class (eg, you can define a distance between two coordinate objects but the same method won't work for distance between two list objects)
***
How to define a new type? 
```
class Coordinate(object):
	# define attributes here
```
* `class`: keyword to define a new type
* `Coordinate`: name of the new type
* `object`: means that `Coordinate` is a Python object and inherits all its attributes, ie
	* `Coordinate` is a subclass of `object`
	* `object` is a superclass of `Coordinate`
***
`__init__` is a special method to initialize data attributes.
```
class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
```
Note: `self` is a parameter referring to an instance of the class.
***
`__init__()` is an example of a **dunder method** (short for *d*ouble *under*score).
* Dunder methods allow us to interact with instances of a class using Python's built-in functions and operators (also called "operator overloading").
* For example:
	* `__str__(self)` allows using the `print()` function
	* `__add__(self, other)`,  `__sub__(self, other)`,  `__eq__(self, other)` and `__lt__(other)` allow using the `+`, `-`, `==` and `<` operators
	* `__len__(self)` allows using the `len()` function
***
How to create a new instance of a class (ie an object)?
```
c = Coordinate(3, 4)
```
or
```
c = Coordinate(y = 4, x = 3)
```
***
How to access an attribute?
```
print(c.x)
```
Use the **dot** operator.
Note: don't provide an argument for `self`, as Python automatically assumes the object on which the method is called is `self`
***
How to define a method?
```
class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance(self, other):
		x_diff_sq = (self.x - other.x) ** 2
		y_diff_sq = (self.y - other.y) ** 2
		return (x_diff_sq + y_diff_sq) ** 0.5
```
* Use `self` to refer to any instance
* Use dot notation to access data
***
How to use a method?
Consider these instances:
```
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
```
The conventional way:
```
print(c.distance(origin))
```
* `c`: object to call method on
* `distance()`: name of method 
* `origin`: parameter (no need to declare `self` since it's implied to be `c`)

is equivalent to:
```
print(Coordinate(distance(c, origin) 
```
* `Coordinate`: name of class
* `distance()`: name of method 
* `c, origin`: parameters, including the object `c` on which to call the method, representing `self`
***
How to print an object's representation?
* By default, `print(<object>)` prints type and memory location, eg outputting `<__main__.Coordinate object at 0x7fa918510488>`
* Define a `__str__()` method for the class, which is called when `print()` is used on a class object
***
`__str__()` must return a string, eg:
```
def __str__(self):
	return "("+str(self.x)+","+str(self.y)+")"
```
Note the use of the `str()` function to convert the number `self.x` to a string.
***
Why do object-oriented programming?
* Bundle data into packages, making them easier to use through custom-built procedures
* Divide and conquer development:
	* test each class independently
	*  reduce complexity, increase readability through modularity
* Reuse code easily
	* Each class has a separate environment, so there's no collision on function names
	* Inheritance allows subclasses to redefine or extend a selected subset of a superclass' behavior
