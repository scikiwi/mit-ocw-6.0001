# Understanding Program Efficiency: 1
Computers are fast/have huge memory and getting faster/more memory, why do time-and space-efficient programs matter?
* Data sets are getting larger too, eg in 2014 Google served 100 million GB worth of pages, so brute force won't work
* Simple solutions may not scale with size in an acceptable manner
***
**Tradeoff between time and space efficiency**:
* Using "lookup" to retrieve pre-computed results (eg in memoized Fibonacci) can reduce time but increase memory requirement
* These lectures focus on time efficiency
***
Measures of a program's time efficiency:
* Time
* Number of atomic operations
* Order of growth of n(operations) with problem size
	* This is the most appropriate measure
***
**Time as a measure of algorithmic efficiency**:
* Good: Running time varies between algorithms
* Bad: Running time varies between implementations
	* Eg if a loop has a couple more steps, running time increases. We want our measure to differ between algorithms, not minor implementational details 
* Bad: Running time varies between computers
	* Faster computers experience shorter running time, whereas we'd want the measure to express just the efficiency of the algorithm
* Bad: Running time isn't predictable on small inputs
	* It takes time to retrieve data from memory
	* For large inputs, the retrieval time increases and inflates running time
	* For running time to be a good efficiency measure, it shouldn't increase for big inputs for non-algorithmic reasons
* Good: Running time varies between inputs
* Bad: Can't really express a relation between inputs and time
	* Because of the above-listed factors:
		* implementational details
		* different computers
		* large inputs having long memory retrieval time
***
**Number of operations as a measure of algorithmic efficiency**:
* Assume these steps take the same, constant time:
	* Mathematical operations (addition, subtraction, multiplication and division)
	* Comparisons
	* Assignments
	* Accessing objects in memory
* Then express the number of operations executed as a function of size of input

```
def celsius_to_f(c):
	return c * 9.0 / 5 + 32
```
has 3 operations, all arithmetic.
```
def sum(x):
	total = 0
	for i in range(x+1):
		total += 1
	return total
```
has 1+3x operations:
* assignment operation: `total = 0`
* 3 operations repeated x times in the loop (3x times total):
	* comparison operation: test in the `for` loop in `i in range(x+1)`
	* arithmetic operation: `total += 1` is really `total = total + 1`, where `total + 1` is an arithmetic operation
	* assignment operation: `total = <updated value>`
***
Is number of operations a good measure of algorithmic efficiency?
* Good: n(ops) varies between algorithms
* Bad: n(ops) varies between implementations
* Good: n(ops) is independent of computers
* Bad: we have no clear definition of which operations to count
* Good: n(ops) varies between inputs
* Good: we can come up with a relationship between input size and n(ops)
***
We'll **focus on the worst case**:
* Different inputs change how the program runs
* When searching for an element `e` in a list `L`:
	* Best case: `e` is first element in `L`
	* Average case: `e` lies halfway between `L`
	* Worst case: `e` is not in `L`
***
**Order of growth as a measure of algorithmic efficiency**:
* Desiderata for an algorithmic efficiency measure:
	* want to evaluate efficiency for **very large inputs**
	* want to know run time as a **function of input size**
	* want to know **"order of" not "exact"** growth; don't need precision
	* want to **ignore machine and implementational details**
	* want a **tight upper bound** on runtime, ie, will **focus on worst case**
***
**Big O notation**:
 * Write n(ops) as a function of input size
 * Focus on dominant term (ie, term that grows most rapidly)
	 * Called evaluating "asymptotic" behavior
 * Ignore multiplicative and additive constants
***
$n^2 + 10000n + 3^{1000}$: O(n²)

$\log n + n + 4$: O(n)

$0.00001n \cdot \log n + 300n$: O(n log n)

$2n^{30} + 2^n$: O(2ⁿ) 
***
**Complexity classes**:
* O(1) is constant run time
* O(log n) is logarithmic run time
* O(n) is linear run time
* O(n log n) is log-linear run time
* O(nᶜ) is polynomial run time (c is constant)
* O(cⁿ) is exponential run time

You want to be as high up in this hierarchy as possible.
***
**Law of Addition for O()**:
* used for **sequential statements**
* O(f(n)) + O(g(n)) = O(f(n) + g(n))
```
for i in range(n):
	print("a")
for j in range(n*n):
	print("b")
```
is O(n) + O(n*n) = O(n + n²) = O(n²)
***
**Law of Multiplication for O()**:
* used for **nested statements**
* O(f(n)) * O(g(n)) = O(f(n) * g(n))
```
for i in range(n):
	for j in range(n):
		print("a")
```
is O(n) * O(n) = O(n*n) = O(n²)
***
Order of growth can be expressed in **multiple variables**, eg O(n * m)
