'''
You are provided X having input features and a target Y as inputs. Assume that the X is n-dimensional.
Fit a linear regression model using the given input X and target Y. Once fitted, obtain the coefficient
of determination for the fitted regression model.

Example 1:
Input:
X = [[8,12,1],[13,4,1],[15,6,1],[9,10,1],[12,1,3]]
Y = [15.3,14.3,15.12,16,16.1]
Output: 0.727506750364747

Example 2:
Input:
X = [[2,1],[4,1],[6,1],[10,1],[1,3]]
Y = [15,14,12,16,11]
Output: 0.5249169435215951

'''

# Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def coeff_of_det(X,Y):
  model = LinearRegression()
  model.fit(X,Y)
  cod = model.score(X,Y)
  return cod
  
print(coeff_of_det(X,Y))
  

