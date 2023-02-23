'''
Fit a logistic regression model using the given input and output patterns X and Y, respectively. Once fitted, determine the accuracy score of this fitted logistic regression model.

Example 1: 
Input:  
X = [[4,2,1],[3,4,6],[5,6,7],[8,9,7]]
Y = [11,12,11,12]
Output: 0.5
 
Example 2:
X = [[1,2,3],[3,4,5],[5,6,7],[8,9,10]]
Y = [11,12,11,12]
Output: 0.5
'''

# My Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def coefficient_of_determination(X,Y):
  model = LogisticRegression()
  model.fit(X,Y)
  pred = model.predict(X)
  s = accuracy_score(Y,  pred)
  return s
  
print(coefficient_of_determination(X,Y))

