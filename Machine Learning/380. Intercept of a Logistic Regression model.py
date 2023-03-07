'''
Fit a logistic regression model using the given input and output patterns X and Y,
respectively. Once fitted, obtain the intercept of this fitted logistic regression model.

Example 1:
Input:
X = [[2,3,3],[3,4,5],[5,6,7],[8,9,10]]
Y = [1,2,1,2]
Output: [-2.27035966]

Example 2:
Input:
X = [[1,2,3],[3,4,5],[5,6,7],[8,9,10]]
y = [11,12,11,12]
Output: [-2.12350588]

'''

# Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
def computing_intercept(X,Y):
  model = LogisticRegression()
  model.fit(X,Y)
  u = model.intercept_
  return u
  
print(computing_intercept(X,Y))
  
