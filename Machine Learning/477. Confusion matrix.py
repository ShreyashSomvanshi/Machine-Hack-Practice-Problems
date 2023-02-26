'''
Consider the input containing ground truth target values as y_true and estimated target value y_pred. 
Return the confusion matrix for the given inputs.

Example 1:
Input:
y_true = [1, 1, 2, 0, 1, 2]
y_pred = [1, 2, 1, 1, 1, 1]
Output:
[[0 1 0]
 [0 2 1]
 [0 2 0]]


Example 2:
Input:
y_true = [1,1,2,1,3,1,0]
y_pred = [0,0,1,1,1,2,2]
Output:
[[0 0 1 0]
 [2 1 1 0]
 [0 1 0 0]
 [0 1 0 0]]
'''


# Solution: 
from sklearn.metrics import confusion_matrix
def ConfusionMatrix(y_true,y_pred):
  return confusion_matrix(y_true,y_pred)
  
print(ConfusionMatrix(y_true,y_pred))

