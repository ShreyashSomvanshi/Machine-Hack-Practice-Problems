'''
A petroleum refining company wants to predict the price of gasoline based on different correlated 
factors like the cost of crude oil, refining cost, marketing cost, fuel tax, etc. You are given the
following training and testing data as inputs containing different feature values. Fit a linear regression
model and a bayesian regression model using the given training data. Once fitted, compare the 
mean squared error value between the models and return the best-fitted regression model based on 
the minimum mean squared error value.

Example 1:
Input:
X_train=[[10.2,9],[18.2,3.3],[14,13],[19,14],[12,23],[16,17]]
X_test=[[10,16],[22,15],[14,23],[22,26]]
y_train=[22.2,44.3,22.4,22.6,34,21.3]
y_test=[22,23,21,20]
Output: LinearRegression

Example 2:
Input:
X_train=[[59,19],[57.7,3],[56,5],[60,4],[52,3],[64,7]]
X_test=[[60,6],[62,5],[54,3],[62,6]]
y_train=[52,44,42.4,42.6,44,41.3]
y_test=[62,63,61,60]
Output: BayesianRidge
'''

# Solution:
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.metrics import mean_squared_error
def MeanAbsoluteError(X_train,X_test,y_train,y_test):
  lr = LinearRegression()
  lr.fit(X_train, y_train)
  lr_pred = lr.predict(X_test)
  lr_err = mean_squared_error(y_test, lr_pred)
  br = BayesianRidge()
  br.fit(X_train, y_train)
  br_pred = br.predict(X_test)
  br_err = mean_squared_error(y_test, br_pred)
  if(br_err < lr_err):
    print('BaysianRidge')
  else:
    print('LinearRegression')
  
MeanAbsoluteError(X_train,X_test,y_train,y_test)  

