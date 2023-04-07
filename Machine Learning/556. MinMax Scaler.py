'''
Transform the given features by scaling each feature to a given range, i.e. between zero and one. 
You are provided with the training data set “data” as input.

Example 1:
Input: data = [[60,62],[62,52],[54,33],[62,62]]
Output:
[[0.75       1.        ]
 [1.         0.65517241]
 [0.         0.        ]
 [1.         1.        ]]

Example 2:
Input: data = [[102,1],[182,3],[114,3],[192,4],[122,2],[116,7]]
Output:
[[0.         0.        ]
 [0.88888889 0.33333333]
 [0.13333333 0.33333333]
 [1.         0.5       ]
 [0.22222222 0.16666667]
 [0.15555556 1.        ]]
 
'''

# Solution:

from sklearn.preprocessing import MinMaxScaler
def minmaxscaler(data):
  scaler = MinMaxScaler(feature_range=(0, 1))
  scaled_data = scaler.fit_transform(data)
  return scaled_data
  
print(minmaxscaler(data))

