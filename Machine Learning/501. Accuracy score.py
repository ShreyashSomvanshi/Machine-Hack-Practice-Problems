'''
A pharmaceutical company plans to perform a machine learning-based prediction of COVID-19 
diagnosis based on various parameters. Consider 1 if the patient suffers from COVID-19 and 
0 if the patient does not suffer from Non-COVID-19. You are provided with training and testing
data as inputs containing various parameters related to COVID-19 diagnosis. Fit a logistic regression
model using the training data. Once fitted, obtain the accuracy score on the test data for the fitted logistic regression model.

Example 1:
Input:
X_train = [[19,2,3],[1,3,4],[1,3,2],[1,4,2],[2,3,4],[6,7,6]]
X_test = [[10,6,2],[1,5,1],[1,3,8],[9,2,6]]
y_train = [0,1,0,1,0,0]
y_test = [1,1,1,0]
Output: 0.75

Example 2:
Input:
X_train =[[10.2,9],[18.2,3.3],[14,13],[19,14],[12,23],[16,17]]
X_test = [[10,16],[22,15],[14,23],[22,26]]
y_train =[0,0,1,1,0,1]
y_test = [0,0,0,1]
Output: 0.5
'''

# Solution:
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def accuracyscore(X_train,X_test,y_train,y_test):
  model = LogisticRegression()
  model.fit(X_train, y_train)
  k=model.predict(X_test)
  return accuracy_score(k,y_test)
  
print(accuracyscore(X_train,X_test,y_train,y_test))

