'''
Consider a vector X containing input features and Y as the target. Assume that the input feature X is multi-dimensional. 
Fit a ridge regression model using the given input X and the target Y. After fitting, obtain the coefficient of the 
fitted ridge regression model as output.

Example 1:
Input:
X = [[8,12,1],[13,4,1],[15,6,1],[9,10,1],[12,1,3]]
Y = [15.3,14.3,15.12,16,16.1]
Output: [-0.07334572  0.04197863  0.48337514]

Example 2:
Input:
X = [[2,1],[4,1],[6,1],[10,1],[1,3]]
Y = [15,14,12,16,11]
Output: [ 0.1827957  -0.92473118]

'''

# Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
def ridge_coefficient(X,Y):
  model = Ridge()
  model.fit(X,Y)
  return model.coef_
  
print(ridge_coefficient(X,Y))
  
