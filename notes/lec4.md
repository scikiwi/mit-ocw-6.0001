# Decomposition, Abstraction, and Functions

A piece of code as a black box -- you want to hide tedious coding details and only want the instructions to use it.
- Achieve **abstraction** by **function specifications** and **docstrings**
- Reusable chunks of code called **functions**
- **Decompose** a problem into sub-problems
- Used together, decomposition and abstraction are powerful as code:
	- can be used many times
	- but only has to be debugged once!
***
By default, function returns `None`, which represents the absence of a value
***
Function can take another function as argument
```
def func():
    print ("inside func")
def func_performer(f):
    print("inside func_performer")
    f()

print(func())
print(func_performer(func))
```
```
Output:

inside func
None
inside func_performer
inside func
None
```
***
Inside a function, a variable defined outside may only be accessed, not modified (you can use global variables, but they [are bad](https://stackoverflow.com/questions/19158339/why-are-global-variables-evil) because they allow functions to have hard-to-predict side effects).

Interesting new term:

[**Spaghetti code**](https://en.wikipedia.org/wiki/Spaghetti_code) (from Wikipedia):  pejorative phrase for unstructured and difficult-to-maintain  source code; the idea is that the flow of control is so complicated that it resembles a bowl of spaghetti.
***
[Python Tutor](http://www.pythontutor.com/) can help you visualize the flow of control in a program by taking you through it step-by-step.
***
Example from lecture (predict the output yourself; if your prediction is incorrect, use PythonTutor)
```
def g(x): 
	def h(): 
		x = 'abc' 
	x = x + 1 
	print('g: x =', x) 
	h() 
	return x 
x = 3 
z = g(x)
```
```
Output:

g: x = 4
```
(At the end of the program, `x` is `3` and `z` is `4`; both are defined in global scope.)

