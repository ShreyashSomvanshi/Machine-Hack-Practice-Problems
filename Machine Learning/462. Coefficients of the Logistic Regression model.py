'''
Consider the iris flower species dataset. The dataset consists of 4 independent features, including sepal and 
petal length and width, respectively, and one target feature specifying the species class. Using these features,
fit a logistic regression model for predicting species class labels of flowers. Once fitted, obtain the model’s coefficients.

Example 1:
Input:
X=[1, 3], [4, 3], [7, 8]
y=[8,5,6]
Output: [[0.35462099 0.59103535]]

Example 2:
Input:
X=[5, 6], [4, 1], [11, 12]
y=[10,20,36]
Output: [[0.266102   0.41815491]]

'''

# Solution: (Rejected while submitting butt accepted in runtime)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
def coefff(X,y):
  Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3, random_state=10)
  model = LogisticRegression()
  model.fit(Xtrain,ytrain)
  cof=model.coef_
  return cof
  
print(coefff(X,y))
