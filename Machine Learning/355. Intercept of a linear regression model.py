'''
Consider a vector X containing input features and Y as the target. Assume that the input
feature X is multi-dimensional. Fit a linear regression model using the given input X and 
the target Y. After fitting, obtain the intercept of the fitted linear regression model as output.

Example 1:
Input:
X = [[1,2],[3,4],[5,1],[1,12],[12,11]]
Y = [6,8,9,10,1]
Output: 9.600264691659667

Example 2:
Input:
X = [[1,2,3],[3,4,5],[5,6,7],[8,9,10]]
Y = [11,12,11,12]
Output: 11.009345794392523

'''

# Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def interceptt(X,Y):
  model=LinearRegression()
  model.fit(X,Y)
  g=model.intercept_
  return g
  
print(interceptt(X,Y))


