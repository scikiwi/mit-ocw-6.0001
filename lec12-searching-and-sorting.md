# Searching and Sorting Algorithms
## Search algorithms
A **search algorithm** is a method for finding an item or a group of items with specific properties within a collection of items.
* It could be an **implicit collection**
	* For example, you could formulate the problem of finding the square root as a search problem with possible algorithmic solutions including:
		* Exhaustive enumeration
		* Bisection search
		* Newton-Raphson
* It could be an **explicit collection**
	* For example, determining if a student record is in a stored collection
## When is the sort worth the cost?
When is **sorting first and then searching** worth it?
* Never worth it for a single search
	* Linear search (best option for an unsorted list) is O(n)
	* Binary search (best option for a sorted list) is O(log n)
	* Sorting first and then searching would be worth it only if 
		* SortingCost + O(log n) < O(n) 
		* ⇒ SortingCost < O(n) - O(log n) 
		* ⇒ **SortingCost < O(n)**
	* Unfortunately, **sorting can never be sub-linear** 
		* Why? Because to sort a collection, you must look at each of its elements at least once
* Could be worth it for multiple searches
	* Pay the overhead of sorting once, then **amortize** the cost of the sort over several searches
	* Worth it if
		* SortingCost + k * O(log n) < k * O(n)
		* ⇒ SortingCost < k * O(n) - k * O(log n)
	* For large enough k, SortingCost becomes irrelevant if it's small enough
## Sort algorithms
### Bogosort
Also called monkey sort, stupid sort, slowsort, permutaton sort, shotgun sort

In **pseudocode**:
* Throw the deck of cards to be sorted into the air
* Pick them up
* Are they sorted?
* Repeat if not sorted

In **code**:
```
def bogo_sort(L):
	while not is_sorted(L):
		random.shuffle(L)
```
Analyzing its **complexity**:
*  **Best case**: **O(n) where n is len(L)** to check if sorted
* **Worst case**: **Unbounded**
### Bubble sort
In **pseudocode**:
* Compare consecutive pairs of elements
* Swap elements in pair such that smaller comes first
* When reach end of list, start over again
* Stop when no more swaps have been made

In **code**:
```
def bubble_sort(L):
	swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j], L[j-1] = L[j-1], L[j]
```
Analyzing its **complexity**:
* The inner `for` loop is for comparisons and is **O(len(L))**
	* For each pass, len(L)-1 comparisons are made, since each adjacent pair is compared
* The outer `while` loop is for doing multiple passes and is **O(len(L))**
	* A property of bubble sort is that after each pass, the largest unsorted element **bubbles** to the end
		* Why does this happen? Because the largest of the as-yet-unsorted elements will survive every comparison in that pass, shifting one position forward each time, until it is compared with the first of the sorted elements
	* So, at most len(L)-1 passes are required
* The **overall complexity** is **O(n²) where n is len(L)**
### Selection sort
In **pseudocode**:
* First step: extract minimum element; swap it with element at index 0
* Subsequent step: in remaining sublist, extract minimum element; swap it with element at index 1
* Properties:
	* At ith step, the list's first i elements are sorted
	* All other elements are bigger than the first i elements

In **code**:
```
def selection_sort(L):
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
```
Analyzing its **complexity** (from [this Programiz page](https://www.programiz.com/dsa/selection-sort)):
| Pass | Number of comparisons |
| :---: | :---: |
| 1st | n-1 |
| 2nd | n-2 |
| 3rd | n-3 |
| … | … |
| last | 1 |
* The total number of comparisons is (n-1) + (n-2) + (n-3 ) + … + 1 = n(n-1)/2. 
* So the complexity is **O(n²)**.
### Merge sort
Merge sort uses a **divide and conquer** approach. In **pseudocode**:
* If list is of length 0 or 1, it's already sorted
* If list has more than one element, split it into two lists, and sort each
* Merge sorted sublists
	* Create an initially empty result list
	* Compare the first element of each sublist; move the smaller to the end of the result list
	* When one list is empty, just copy the rest of the other list to the end of the result

An **example** of merging:
| Left in list 1 | Left in list 2 | Comparison | Result list
| :--- | :--- | :--- | :--- |
|[1, 5, 18, 19, 20]|[2, 3, 4, 17]|1, 2|[]|
|[5, 18, 19, 20]|[2, 3, 17]|5, 2|[1]|
|[5, 18, 19, 20]|[3, 17]|5, 3|[1, 2]|
|[5, 18, 19, 20]|[17]|5, 17|[1, 2, 3]|
|[18, 19, 20]|[17]|18, 17|[1, 2, 3, 5]|
|[18, 19, 20]|[]|18, ---|[1, 2, 3, 5, 17]|
|[]|[]||[1, 2, 3, 5, 17, 18, 19, 20]|

The merging step in **code**:
```
def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
	return result 
```
Analyzing **complexity of the merge step**:
* We go through two lists, with just one pass through each list
* We copy O(len(left) + len(right)) elements to the results list
* We make O(len(longer list)) comparisons
* Thus, merging is O(len(left) + len(right)) + O(len(longer list)
* Or, **merging is linear in length of the lists**

Merge sort in **code**:
```
def merge_sort(L):
	if len(L) <= 1:
		return L[:] # returns a copy of L
	else:
		middle = len(L) // 2
		left = merge_sort(L[:middle])
		right = merge_sort(L[middle:])
		return merge(left, right)
```
* The principle is dividing the list successively into halves
* This algorithm is depth-first such that it conquers the smallest pieces down one branch first before moving to larger pieces

Analyzing complexity of **merge sort**:
* At first recursion level
	* There are n/2 elements in each of the two lists
	* One merge needs to be made
		* n comparisons (each element in both the limits is compared exactly once)
		* n copying operations
* At second recursion level
	* There are n/4 elements in each of the four lists
	* Two merges need to be made
		* n comparisons (each element in all four lists is compared exactly once)
		* n copying operations
* **Each recursion level** is **O(n) where n is len(L)**
* Each recursive call divides list in half, so the **number of recursive calls** is **O(log n) where n is len(L)**
* **Overall complexity** is **O(n log n) where n is len(L)**

Merge sort has the **fastest worst case** of any sorting algorithm, ie, O(n log n) 
