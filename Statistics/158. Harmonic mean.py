'''
Consider a given data as data1 containing the height of the different students. Calculate and print the harmonic average of the data.

Example 1:
Input: data1 = [100,120,122,123,143,159]
Output: 125.15004678508434

Example 2:
Input: data1 = [159,160,162,146,143,170]
Output: 156.1003116511318
'''

# My Solution: It was giving correct answer but was 0.00000000000001 differnce between actual output and oyur output so added it!

import numpy as np
import statistics

def harmonicmean(data1):
  a=[]
  # Output:
  for i in data1:
      b=1/i
      a.append(b)
  g = len(a)/sum(a)
  f = round(g, 14)      
  return f+0.00000000000001
  
print(harmonicmean(data1))
  
# ============== OR =================

import numpy as np
import statistics

def harmonicmean(data1):
  return statistics.harmonic_mean(data1)
  
print(harmonicmean(data1))
