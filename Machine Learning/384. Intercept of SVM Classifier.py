'''
Fit a support vector machine classification model using the given input and output patterns X and Y, respectively.
Once fitted, obtain the intercept of this fitted SVM classifier.

Example 1:
Input:
X=[7, 2], [8,6], [5,7]
Y=[2,1,2]
Output: [0.67688972]

Example2:
Input:
X=[7, 2], [8,6], [5,7]
Y=[2,1,1]
Output: [-0.43025481]
'''

# Solution:
import pandas as pd
import numpy as np
from sklearn.svm import SVC
def computing_intercept(X,Y):
  model=SVC()
  model.fit(X,Y)
  g=model.intercept_
  return g
  
print(computing_intercept(X,Y))

