# Iterators and Generators

from pathlib import Path

# Example 1: Iterate over a list:

my_list = ["These", "are", "some", "words"]

for s in my_list:
    print(s)
    
# These
# are
# some
# words

# Example 2: Iterate over a String

for c in "python":
    print(c)
    
# p
# y
# t
# h
# o
# n    

# Example 3: Iterate over a dictionary:
my_dict = {"x":1, "y":2, "z":3}
for k,v in my_dict.items():
    print(k,v)
    
# x 1
# y 2
# z 3    

# Example 4: Iterate over a file:

# Get the directory where this script lives
file_path = Path(__file__).parent / "a.txt"

with open(file_path) as f:
    for line in f.readlines():
        print(line[:-1])
# This
# is
# a
# text
# file
# with
# random
# dat

# Example 5: Create an iterator from an iterable object (list here) using the built-in function iter()

x = iter([1,2,3,4,5])

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# Example 6: Let's create an iterator of our own:
class yrange:
    def __init__(self, n):
        self.i = n
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()
            
my_r = yrange(5)
print(next(my_r))
print(next(my_r))
print(next(my_r))
print(next(my_r))
print(next(my_r))


# Example 7: Generators: It is an simpler way to create an iterator.

def myrange(n):
    i = 0
    while i<5:
        yield i
        i += 1
        
my_r = myrange(5)
print(next(my_r))
print(next(my_r))
print(next(my_r))
print(next(my_r))
print(next(my_r))

# 0
# 1
# 2
# 3
# 4

# Example 8: 

def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")
    

f = foo()
next(f)
next(f)
next(f)

# begin
# before yield 0
  
# Example 9:
def integers():
    i = 1
    while True:
        yield i
        i = i + 1
        
ints = integers()
for i in range(5):
    print(next(ints))
    
# Example 10:
def squares():
    for i in integers():
        yield i*i
sqs = squares()
for i in range(5):
    print(next(sqs))
    
# 1
# 4
# 9
# 16
# 25