'''
A bird conservation organisation plans to perform a machine-learning-based predictive
analysis on the life span of different birds based on various parameters like body size,
metabolic rate, body temperature, glucose content in the body, etc. You are given the 
following training and testing data as inputs containing these parameters. Fit a 
linear regression model using the training. Once fitted, obtain the mean absolute error
value on the test data for the fitted linear regression model.

Example 1:
Input:
X_train =[[.9,.2,.9],[.6,.2,.3],[.4,.4,.3],[.3,.9,.4],[.3,.2,.3],[.6,.6,.7]]
X_test = [[.5,.3,.6],[.7,.2,.5],[.6,.4,.3],[.7,.2,.6]]
y_train =[8,6,3,4.5,2,1]
y_test = [4,4.5,4,5]
Output: 1.4967159277504103

Example 2:
Input:
X_train =[[.9,.2],[.2,.3],[.4,.3],[.9,.4],[.2,.3],[.6,.7]]
X_test = [[.5,.3],[.7,.2],[.4,.3],[.2,.6]]
y_train =[11,5,7,13,5,13]
y_test = [8,9,7,8]
Output: 1.1102230246251565e-15
'''

# Solution:
# Mean Absolute Error for linear regression model
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
def MeanAbsoluteError(X_train,X_test,y_train,y_test):
  lr = LinearRegression()
  lr.fit(X_train, y_train)
  ypred = lr.predict(X_test)
  return mean_absolute_error(ypred, y_test)
  
print(MeanAbsoluteError(X_train,X_test,y_train,y_test))
