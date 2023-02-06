# Written on my own, before looking 
# at the example in Lecture 6

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("n: "))
print(fib(n))
