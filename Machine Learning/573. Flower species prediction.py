'''
Consider the iris flower species dataset. The dataset consists of 4 independent features, including sepal and 
petal length and width, respectively, and one target feature specifying the species class. You are provided with
input data named “test” containing feature values. Fit a logistic regression model using the provided iris dataset
and return the prediction of species class labels of flowers based on the given input.

Example 1:
Input: test= [[6.7, 3.1, 4.7, 1.5]]
Output: [1]

Example 2:
Input: test= [[5.9, 3. , 5.1, 1.8]]
Output: [2]
'''

# Solution:
import warnings
warnings.filterwarnings("ignore")

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def iris_prediction(test):
  iris = load_iris()
  X = iris.data
  y = iris.target
  Xtn, Xts, ytn, yts = train_test_split(X,y,random_state=1)
  model = LogisticRegression()
  model.fit(Xtn,ytn)
  p = model.predict(test)
  return p
  
print(iris_prediction(test))
  
