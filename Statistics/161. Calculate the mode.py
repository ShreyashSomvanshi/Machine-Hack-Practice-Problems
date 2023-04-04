'''
Find the model of a given data data1 that consists of the speeds of a car.

Example 1:
Input: data1 = [45,46,47,48,46]
Output: 46

Example 2:
Input: data1 = [115,123,97,98,126,115]
Output: 115

'''

# Solution:

import statistics
def mostFrequentdata(data1):
  return statistics.mode(data1)
  
print(mostFrequentdata(data1))
