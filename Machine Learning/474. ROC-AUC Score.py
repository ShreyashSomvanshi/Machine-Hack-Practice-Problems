'''
You are given an input containing input features X and a target Y. Fit a logistic regression model
using the given input X and the target Y. After fitting, compute the area under the receiver operating
characteristic curve score (ROC-AUC Score) from the model predictions.

Example 1:
Input:
X = [[1,1],[1,1],[6,1],[11,1],[11,3]]
Y = [0,0,1,0,0]
Output: 0.5

Example 2:
Input:
X = [[1,2],[1,3],[1,3],[1,4],[2,3],[6,7]]
Y = [0,0,1,0,1,1]
Output: 0.8333333333333333

Constraints:
Target Y contains binary class

'''

# Solution:
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
 
def RocAucScore(X,Y):
  model = LogisticRegression()
  model.fit(X,Y)
  l = model.predict(X)
  x = roc_auc_score(Y,l)
  return x
  
print(RocAucScore(X,Y))
  
