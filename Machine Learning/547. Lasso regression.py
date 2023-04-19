'''
A weather forecasting company wants to predict the temperature in terms of °F Fahrenheit based on different
parameters like wind, humidity, precipitation, etc. The company decides to use a machine learning-based approach
to predict the temperature. You are provided with the following training and testing data as inputs. Fit a lasso
regression model using the training data. Once fitted, obtain the R2 value on the test data for the fitted regression model.

Example 1:
Input:
X_train=[[1,9],[2,11],[3,13],[4,15],[5,17],[6,19]]
X_test=[[7,21],[8,23],[9,25],[10,27]]
y_train=[22,23,24,25,26,27]
y_test=[28,29,30,31]
Output: 0.38285714285714234

Example 2:
Input:
X_train=[[10,9],[20,11],[30,13],[40,15],[50,17],[60,19]]
X_test=[[70,21],[80,23],[90,25],[100,27]]
y_train=[42,43,44,45,46,47]
y_test=[48,49,51,52]
Output: 0.7053714285714279

'''

# Solution:

from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
def r2_squared(X_train,X_test,y_train,y_test):
  model = Lasso()
  model.fit(X_train, y_train)
  pred = model.predict(X_test)
  r2 = r2_score(y_test,pred)
  return r2
  
print(r2_squared(X_train,X_test,y_train,y_test))
