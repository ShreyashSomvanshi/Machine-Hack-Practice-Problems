'''
You are given an input containing input features X and a target Y. Consider that the input feature is N-dimensional.
Fit a linear regression model using the given input X and the target Y.After fitting, compute the coefficient for the
prediction of each of the target values as output.

Example 1:
Input:
X = [[10,12],[13,41],[15,11],[11,12],[12,12]]
Y = [6,8,9,10,1]
Output: [0.36846002 0.03660744]

Example 2:
Input:
X = [[10,2,3],[31,4,5],[15,6,7],[3,9,10]]
Y = [11,12,11,12]
Output: [0.0269601  0.07129542 0.07129542]

'''

# Solution:
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def coeff(X,Y):
  model=LinearRegression()
  model.fit(X,Y)
  g=model.coef_
  return g
  
print(coeff(X,Y))



