# Tuples, Lists, Aliasing, Mutability, and Cloning
How to create an empty tuple:
```
tup = ()
```
***
How to create a tuple with one element:
```
tup = (0,)
```
You need the extra comma at the end.
***
You can slice tuples in exactly the same way as strings are sliced, i.e., `tup[start:stop:step]`.
***
`tup[1] = 0` gives an error, as the object `tuple` cannot be modified.
***
To combine lists together, 
- use **concatenation**, `+` operator, to **give you a new list**
- use `L.extend(some_list)` to **mutate** the list in place

Example:
```
L1 = [1, 2, 3]
L2 = [4, 5, 6]
```
- `L3 = L1 + L2` means `L3` is now `[1, 2, 3, 4, 5, 6]`
- `L1.extend([4, 5])` means `L1` is now mutated to `[1, 2, 3, 4, 5]`

**Important**: `list.extend()` takes exactly one argument, a `list`.
***
Operations to remove elements from list:

- delete element at **specific index** with `del(L[index])`
- remove (and return) element at **end of list** with `L.pop()` 
	*	`L.pop(index)` removes (and returns) element at **specific index**	
- remove a **specific element** with `L.remove(element)`
	* looks for the element and removes it
	* if element occurs multiple time, **removes the first occurrence**
	* if element not in list, gives error	
***
Sorting (in increasing order) lists:
* `L.sort()` **mutates** list
* `sorted(L)` returns sorted list, **does not mutate**

`L.reverse()` sorts in decreasing order, **mutates** list
***
Important to remember that in Python, variables are only pointers to objects.
```
x = [1, 2, 3]
y = x
y.append(4)
print("y:", y)
print("x:", x)
```
```
Output:

y = [1, 2, 3 ,4]
x = [1, 2, 3, 4]
```
After `y = x`, any changes to `y` will also affect `x`.
***
`y` is a second name, an **alias**, given to the same piece of data.
***

To avoid getting a pointer to the same list, **clone** the list: copy every element using `y = x[:]`
***
Avoid mutating a list as you are iterating over it.
```
Incorrect:

def remove_dups(L1, L2): 
	for e in L1: 
		if e in L2: 
			L1.remove(e) 
L1 = [1, 2, 3, 4] 
L2 = [1, 2, 5, 6] 
remove_dups(L1, L2)
```
```
Correct:

def remove_dups(L1, L2): 
	L1_copy = L1[:] 
	for e in L1_copy: 
			if e in L2:
				L1.remove(e)
```
