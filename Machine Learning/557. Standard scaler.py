'''
You are provided with the training data set, “data”, as input. Standardize the features by removing mean 
and scaling to unit variance using appropriate scaling technique and return the transformed data.

Example 1:
Input: data = [[59,10],[57.7,3],[56,5],[60,4],[52,3],[64,7]]
Output:
[[ 0.24040052  1.87082869]
 [-0.11339647 -0.93541435]
 [-0.57605407 -0.13363062]
 [ 0.51255204 -0.53452248]
 [-1.66466018 -0.93541435]
 [ 1.60115816  0.6681531 ]]


Example 2:
Input: data = [[60,6],[62,5],[54,3],[62,6]]
Output:
[[ 0.15249857  0.81649658]
 [ 0.76249285  0.        ]
 [-1.67748427 -1.63299316]
 [ 0.76249285  0.81649658]]

'''

# Solution:

from sklearn.preprocessing import StandardScaler
def Standardscaler(data):
  std_scaler = StandardScaler()
  scaled_data = std_scaler.fit_transform(data)
  return scaled_data
  
print(Standardscaler(data))
  
  
  
