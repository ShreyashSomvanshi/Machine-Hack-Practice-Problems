'''
Predict the stock price based on different factors like dividends, financial performance, supply and demand, etc. 
You are provided with training and testing data as inputs. Fit a ridge regression model using the training data. 
Once fitted, obtain the stock price prediction on the test data for the fitted ridge regression model.

Example 1:
Input:
X_train =[[25],[26],[35],[27],[28],[29]]
X_test = [[26.6]]
y_train =[1002,1065,1364,1363,1080,1119]
Output: [1116.00569948]

Example 2:
Input:
X_train =[[125],[126],[235],[227],[128],[229]]
X_test = [[266]]
y_train =[2002,3065,2364,3363,2080,2119]
Output: [2677.35581948]

'''

# Solution:

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
def stock_price(X_train,X_test,y_train):
  model = Ridge()
  model.fit(X_train,y_train)
  d = model.predict(X_test)
  return d
  
print(stock_price(X_train,X_test,y_train))
