'''
An automobile manufacturing company wants to predict the mileage of automobiles based on 
various factors related to the performance of the automobile. You are given the following
training and testing data as inputs which hold the features and target variable needed for
the prediction. Fit a linear regression model using the training data. Once fitted, obtain
the R2 value on the test data to understand the goodness-of-fit measure for the fitted linear regression model.

Example 1:
Input:
X_train=[[10.2,9],[18.2,3.3],[14,13],[19,14],[12,23],[16,17]]
X_test=[[10,16],[22,15],[14,23],[22,26]]
y_train=[22.2,44.3,22.4,22.6,34,21.3]
y_test=[22,23,21,20]
Output: -17.73259257306234

Example 2:
Input:
X_train=[[102,11],[182,33],[114,13],[192,14],[122,23],[116,17]]
X_test=[[130,16],[122,15],[114,23],[122,26]]
y_train=[222,243,224,226,342,213]
y_test=[222,232,212,202]
Output: -18.010825281109636

'''

# Solution:
#R2 for a linear regression model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def r2_squared(X_train,X_test,y_train,y_test):
  model = LinearRegression()
  model.fit(X_train, y_train)
  d=model.predict(X_test)
  r = r2_score(y_test,d) # r square error 
  return r
  
print(r2_squared(X_train,X_test,y_train,y_test))
