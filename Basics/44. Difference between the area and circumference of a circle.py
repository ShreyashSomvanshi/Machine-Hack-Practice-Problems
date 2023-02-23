'''
Consider the radius of a circle as R. First, Calculate the area and circumference of the circle separately and then 
obtain the difference between the area and circumference of a circle. Assume the value of pi is 3.14 units.

Example 1: 
Input:  R = 5
Output: 47.099999999999994
 
Example 2: 
Input: R = 4
Output: 25.12
'''

# My Solution:
pi = 3.14

def diffAreaCircumference(R):
  area = pi*R*R
  cirfrnc = 2*pi*R
  diff = area - cirfrnc
  return diff
  
print(diffAreaCircumference(R))
