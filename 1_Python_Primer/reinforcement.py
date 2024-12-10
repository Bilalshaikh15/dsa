from random import randrange

# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def isMultiple(n,m):
    return True  if(m%n == 0) else False
    
# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def isEven(k):
    return True if(k%2==0) else False

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    max=0
    min = data[0]
    for el in data:
        if el>max:
            max=el
        if el<min:
            min=el
    return(min,max)

# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
def sumSquare(n):
    sum=0
    for i in range(1,n):
        sum = sum +  (i*i)
    return sum

# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
def sumSquareList(n):
    return sum([ k*k for k in range(1,n)])

# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.
def OddsumSquare(n):
    return sum([k*k if k%2!=0 else 0  for k in range(1,n)])

# R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
def OddsumSquare(n):
    return sum([k*k if k%2!=0 else 0  for k in range(1,n)])

# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?
# Answer : Negative index k + len(string) = j positive index of string ,
# where string[-k] == string[j]

# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
def range1():
    for i in range(50,90,10):
        print(i)

# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
def range2():
    for i in range(8,-10,-2):
        print(i)

# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
def sumSquareOf2():
    return [2**k for k in range(0,9)]

# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
def myChoice(arr):
    randomIndex = randrange(0,len(arr))
    return arr[randomIndex]

