import numpy as np

x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])

# Number of Data
print(len(x))

# Sample Average
print(np.mean(x))

# Sample Variance
print(np.var(x))

# Sample Standard Variance
print(np.std(x))

# Maximum and Minimum
print(np.max(x))
print(np.min(x))

# Median
print(np.median(x))

# Quartile
print(np.percentile(x, 0)) # Minimum, 0%
print(np.percentile(x, 25)) # 1/4, 25%
print(np.percentile(x, 50)) # 2/4, 50%
print(np.percentile(x, 75)) # 3/4, 75%
print(np.percentile(x, 100)) # Maximum, 100%