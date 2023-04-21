'''
You are provided with the training data set, “data”, as input. Assume that the “data” has ceratin outliers. 
Perform scaling on this data according to the quartile range to be more robust to the outliers. Once scaled, 
return the transformed data as output.

Example 1:
Input: data = [[ 100,2],[1000,12],[646,2.3],[483,42.3]]
Output:
[[-1.33765299 -0.29682997]
 [ 1.25413967  0.2795389 ]
 [ 0.23470122 -0.2795389 ]
 [-0.23470122  2.0259366 ]]

Example 2:
Input: data = [[231,60,10],[432,22,62],[223,44,54],[217,78,62]]
Output:
[[ 0.06694561  0.30769231 -2.52631579]
 [ 3.43096234 -1.15384615  0.21052632]
 [-0.06694561 -0.30769231 -0.21052632]
 [-0.16736402  1.          0.21052632]]
'''

# Solution:

from sklearn.preprocessing import RobustScaler
def robustscaler(data):
  scaler = RobustScaler()
  data = scaler.fit_transform(data)
  return data
  
print(robustscaler(data))
  
