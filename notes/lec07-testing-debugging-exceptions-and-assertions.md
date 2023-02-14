


# Testing, Debugging, Exceptions, and Assertions
From the start, design code to ease debugging:
* Break program up into modules that can be tested and debugged individually
* Write out input and output constraints on modules
* Write out assumptions behind code design
***
Don't rush into **integration testing** -- checking if overall program works correctly -- before **unit testing** -- checking if each module works correctly.
***
How to debug?
* Use [Python Tutor](https://pythontutor.com/)
* Use built-in debuggers in IDLE and Anaconda
* `print` statement
	* I think using `print` to debug is somewhat looked down upon today when modern debugging tools are available (see for example [this StackExchange answer](https://stackoverflow.com/a/189570)
* use your brain, be systematic
***
**Important tip**: don't write the entire program at once and try debugging it. Instead, write a function, test and debug it, repeat, then do integration testing.
***
Common Python exceptions:
* `IndexError`: trying to access beyond list limits, eg referencing `test[4]` for `test = [1, 7, 4]`
* `Type Error`: trying to convert an inappropriate type (eg `int(test)`) or mixing data types without coercion (eg `'a'/4`)
* `ValueError`: operand has the correct type, but value is illegal (eg trying to convert a string like `"lol"` to an `int` using `int()`)
* `NameError`: referencing a non-existing variable, eg `a`
* `NameError`: local or global name not found
* `SyntaxError`: Python can't parse program
* `IOError`: IO system reports malfunction (eg file not found)
* `AttributeError`: attribute reference fails
***
Consider the following code:
```
a = int(input("a: "))
b = int(input("b: "))
print(a/b)
```
How do we "handle" any exceptions? With the `except` handler:
```
try:
	a = int(input("a: "))
	b = int(input("b: "))
	print(a/b)
except:
	print("Bug encountered.")
```
Exceptions raised by any statement in the body of `try` are "handled" by the `except` statement and execution continues with the body of the `except` statement.
***
Can we `print` more specific error messages? Two obvious exceptions: 
* `ValueError`: user-inputted value cannot be converted to an `int`
* `ZeroDivisionError`: `b` is zero, leading to an attempt at division by zero
```
try:
	a = int(input("a: "))
	b = int(input("b: "))
	print(a/b)
except ValueError:
	print("Couldn't convert to a number.")
except ZeroDivisionError:
	print("Can't divide by zero.")
except:
	print("Something went very wrong.")
```
***
* `else`
	* body of this is executed when body of `try` executes with no exceptions
* `finally`
	* body of this is always executed after `try`, `else` and `except`, even if they raised another error or executed a `break`, `continue` or `return`.
	* useful for clean-up code that should run regardless what else happen (eg close a file)
***
`raise` throws an error.
[This StackExchange answer](https://stackoverflow.com/a/56942544/21174206) does a great job explaining the difference between `raise SomeException`, `except:` and `except SomeException:`. 
The syntax is:
```
raise SomeError("error text")
```
***
 `assert` throws an error *if* some condition is met. 
```
def avg(grades): # grades is a list containing test scores
	assert len(grades) != 0, "no grades data"
	return sum(grades)/len(grades)
```
Here `assert` throws an `AssertionError` if given an empty list for grades, stopping execution of the program. Otherwise, execution moves on to the next line of the program.
***
**Why use assertions?**
* Assertions don't allow a programmer to control the response to unexpected conditions. Rather, they ensure that execution halts whenever an expected condition isn't met.
* Typically used to check inputs to functions (like above while checking if `grades` is an empty list).
* Can be used to check outputs of a function to avoid propagating bad values.
* Can make it easier to trace the source of a bug.
***
**Where to use assertions vs exceptions**
* With assertions, the goal is to spot bugs as soon as they're introduced and make clear where they happened, so that debugging becomes fast. They're a supplement to *testing* code.
* With exceptions, the goal is to avoid bad data input from users (I'm guessing this is because you don't want them to see an `AssertionError`, and rather want the error message to be a line of `print`ed text).
* Use assertions to:
	* check types of arguments or values
	* check that invariants on data structures are met
	* check constraints on return values
	* check for violations of constraints on procedure (eg no duplicates in a list) 
