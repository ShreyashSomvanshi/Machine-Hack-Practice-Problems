'''
Consider a multi-dimensional array X having input features and a one-dimensional array Y as the target.
Fit a linear regression model using the given input X and target Y. Once fitted, predict the target value for 
a given set N containing feature values as input. 

Example 1: 
Input:  
X = [[2.2,10],[3,4],[5,6],[9,10]]
Y = [13.1,11.1,10.12,12]
N = [[1,2]]
Output: [10.16]
 
Example 2: 
Input: 
X = [[8,12,1],[13,4,1],[15,6,1],[9,10,1],[12,1,3]]
Y = [15.3,14.3,15.12,16,16.1]
N = [[10,2,2],[11,12,1]]
Output: [14.97174825 16.00685315]
'''

# Solution:
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def modell(X,y,N):
    model = LinearRegression()
    mod = model.fit(X,y)
    y = mod.predict(N)
    return y

print(modell(X,Y,N))


# My Approach:
'''
import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
def modell(X,y,N):
    model = LinearRegression()
    mod = model.fit(X,y)
    y = mod.predict(N)
    return y

X = [[2.2,10],[3,4],[5,6],[9,10]]
Y = [13.1,11.1,10.12,12]
N = [[1,2]]
# Output: 
print(modell(X,Y,N))
# [10.16]

'''
