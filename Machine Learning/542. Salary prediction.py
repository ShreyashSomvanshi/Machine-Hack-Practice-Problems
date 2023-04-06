'''
A micro-enterprise plan to make machine-learning-based prediction of the salary of its employees
based on their years of experience. You are provided with the following training and testing data
as inputs. Fit a linear regression model using the training. Once fitted, obtain the salary prediction
on the test data for the fitted linear regression model.

Example 1:
Input:
X_train =[[1],[2],[3],[4],[5],[6]]
X_test = [[7]]
y_train =[1000,2000,3000,4000,5000,6000]
Output: [7000.]

Example 2:
Input:
X_train =[[10],[12],[13],[14],[15],[16]]
X_test = [[7]]
y_train =[30,12,15,34,50,40]
Output: [5.28571429]

'''

# Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def salary_prediction(X_train,X_test,y_train):
  reg = LinearRegression().fit(X_train, y_train)
  y_test_pred = reg.predict(X_test)
  return y_test_pred
  
print(salary_prediction(X_train,X_test,y_train))
