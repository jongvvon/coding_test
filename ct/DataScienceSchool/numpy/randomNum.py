import numpy as np

np.random.seed(0) # seed(x), x >= 0
print(np.random.rand(5))
print(np.random.rand(10))

np.random.seed(0) # reset
print(np.random.rand(5))
print(np.random.rand(10))

# suffle of data
x = np.arange(10)
print(x)
np.random.shuffle(x)
print(x)

# Data Sampling
# numpy.random.choice(a, size=None, replace=True, p=None)
# a : data(if only R, arange(a)), size = sample number(R), 
# replace = Boolean(True is duplicate possible), p = array(probability)
print(np.random.choice(5, 5, replace=False)) # == shuffle
print(np.random.choice(5, 3, replace=False)) # choose 3(non-duplicate)
print(np.random.choice(5, 10)) # choose 5 (duplicate)
print(np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0])) # probability settings

# Random Number Generate
print(np.random.rand(10))   # rand is generate 0 < Num < 1
print(np.random.rand(3, 5)) # size settings

print(np.random.randn(10))   # randn is expected value = 0 and
print(np.random.randn(3, 5)) # standard deviation= 1

# randint
# numpy.random.randint(low, high=None, size=None)
# if high=None, 0 to low
# else low to high
print(np.random.randint(10, size=10))
print(np.random.randint(10, 20, size=10))
print(np.random.randint(10, 20, size=(3, 5)))

# Real Number Data Counting
# if Random Number is R, unique and bincount are data counting
print(np.unique([11, 11, 2, 2, 34, 34])) # unique erase duplicate data 

# return_counts is to print num of data
a = np.array(['a', 'b', 'b', 'c', 'a'])
index, count = np.unique(a, return_counts=True)
print(index)
print(count)

# bincount, 0 to minlength-1 each data of num check
# unique isn't supposed
print(np.bincount([1, 1, 2, 2, 2, 3], minlength=6))