'''
Consider a tuple. Return the tuple pairs.

Example 1:
Input: x = ('M', 'H', "K")
Output: [('M', 'H'), ('M', 'K')]

Example 2:
Input: x = ('A','S','R','X')
Output: [('A', 'S'), ('A', 'R'), ('A', 'X')]

'''

# Soln: #1 28ms 

from itertools import product
def Tuple(X):
    
# Define some example input iterables
    first = list(X[0])
    other = list(X[1:len(X)])

    # Compute the Cartesian product
    combinations = list(product(first, other))

    # Print the result
    return combinations

print(Tuple(x))
