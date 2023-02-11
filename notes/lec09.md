# Python Classes and Inheritance
How to access a data attribute?
* You could use `ObjectName.Data`, but it's not recommended
* Use a **getter** function: `ObjectName.getData()`

Implement a getter function:
```
def getData(self):
	return self.Data
```
***
How to set a data attribute?
* Don't use `ObjectName.Data = new_value`
* Use a **setter** function: `ObjectName.setData(Data)`

Implement a setter function:
```
def setData(self, value)
	self.Data = Data
```
***
The principle of **information hiding**:
* Outside of a class, use getters and setters (ie, `ObjectName.getData()` not `ObjectName.Data`)
* This is because the author of a class definition may change data attribute variable names, eg:

```
class newClass(object):
	def __init__(self, Data):
		self.Value = Data
```
Here, the author changed `self.Data` to `self.Value`, making the call `ObjectName.Data` outside the class invalid. Using getters and setters:
* makes code easy to maintain (you can edit data attribute variable names within a class without worrying about code outside the class)
* prevents bugs
* is good style
***
Python isn't great at information hiding:
* allows you to **access data** from outside class definition
	* `print(coord.x)`
* allows you to **write to data** from outside class definition
	* `coord.x = "infinite"`
* allows you to **create new data attributes** for an instance from outside class definition
	* `coord.size = "large"`

It's not good style to do any of these.
***
How does **inheritance** work? Consider this parent class:
```
class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None
	# getters for age and name
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	# setters for age and name
	def set_age(self, newage):
		self.age = newage
	def set_name(self, newname=""):
		self.name = newname
	def __str__(self):
		return "animal:"+str(self.name)+":"+str(self.age)
```
Here, the superclass `object` implements basic Python operations like binding variables, etc.
Consider `Animal`'s subclass `Person`:
```
class Person(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, age)
		self.set_name(name)
		self.friends = []
	def get_friends(self):
		return self.friends
	def add_friend(self, fname):
		if fname not in self.friends:
			self.friends.append(fname)
	def speak(self):
		print("hello")
	def __str__(self):
		return "person:"+str(self.name)+":"+str(self.age)
```
Notice:
* we added the **new attributes** `speak()` , `get_friends()` and `add_friend()`
	* can be called on `Person` instance
	* throws error if called on `Animal` instance
* `Person` **inherits** parent class' attributes, ie `__init__()`, `age`, `name`, `get_age()`, `get_name()`, `set_age()`, `set_name()` and `__str__()`
* new `__str__()` and `__init__()` **overrides** that of `Animal`

How does new `__init__()` work?
* `Animal.__init__(self, age)` calls the `Animal` constructor
* `self.set_name(name)` calls `Animal`'s method
* `self.friends = []` adds a new data attribute, which is used in `get_friends()` and `add_friend()`
***
Since a subclass can have methods with the same name as in the superclass but different body (eg `__str__()` above), it's worth clarifying which named method takes precedence
* For an instance of a class, look for a method name in the current class definition
* If not found, look for method name up the hierarchy (in parent class, grandparent class, and so on)
* The first method up the hierarchy that you found with the method name takes precedence
