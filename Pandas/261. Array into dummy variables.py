'''
You are given a data named data1, which is array_like. Assume that the input data is made up of an n-number of categorical variables. Convert the given input data into dummy variables.

Example 1:

Input: data1 = [1,2,3]
Output:
   1  2  3
0  1  0  0
1  0  1  0
2  0  0  1

Example 2:
Input: data1 = [1,1,1,2]
Output:
   1  2
0  1  0
1  1  0
2  1  0
3  0  1

Hints: Use pandas get_dummies() method.
'''

# Soln:
import pandas as pd
def dummyVariable(data1):
  return pd.get_dummies(data1)
  
print(dummyVariable(data1))

