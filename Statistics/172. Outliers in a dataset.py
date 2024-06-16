'''
Consider data as data1 comprising n number of integers. Detect outliers in this given data using the IQR method.

Example 1:
Input: data1 = [1,2,3,4,5,6,-12,28]
Output: [-12, 28]

Example 2:
Input: data1 = [-122,29,27,25,26,29,28,90,22.2,19.09]
Output: [-122, 90]
'''

# Soln1:

import numpy as np
def outlierDetection(data1):
  Q1 = np.percentile(data1, 25)
  Q3 = np.percentile(data1, 75)
  IQR = Q3 - Q1
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR
  outliers = [x for x in data1 if x < lower_bound or x > upper_bound]
  return outliers
  
print(outlierDetection(data1))
