'''
Fit a ridge classification model using the given input and output patterns X and y, respectively.
Once fitted, obtain the intercept of this fitted Ridge classifier.

Example 1:
Input:
X=[7, 4], [2,6], [9,7]
Y=[3,1,3]
Output: [-0.51315789]

Example 2:
Input:
X=[2, 4], [8,6], [9,1]
Y=[4,1,4]
Output: [2.91659427]
'''

# Solution:
import pandas as pd
import numpy as np
from sklearn.linear_model import RidgeClassifier
def computing_intercept(X,Y):
  model=RidgeClassifier()
  model.fit(X,Y)
  i = model.intercept_
  return i
  
print(computing_intercept(X,Y))
