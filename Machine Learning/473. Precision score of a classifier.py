'''
Consider the ground truth target values y_true and estimated target values y_pred as inputs. 
Obtain the precision score for the given y_true and y_pred.

Example 1:
Input:
y_true = [0, 1, 1, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 1]
Output: 0.25

Example 2:
Input:
y_true = [1, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 0, 1]
Output: 0.5

Constraints: y_true and y_pred contain binary classes
'''

from sklearn.metrics import precision_score
def PrecisionScore(y_true,y_pred):
  return precision_score(y_true, y_pred)
  
print(PrecisionScore(y_true,y_pred))
