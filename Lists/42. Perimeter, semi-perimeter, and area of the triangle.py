'''
Consider a triangle having its sides x, y, and z where these values are integers. Calculate and print the triangle's area, perimeter,
and semi-perimeter in a list in the following order [ area,  perimeter, semi-perimeter].

Example 1: 
Input: x,y,z = 10,20,15
Output: [72.61843774138907, 45, 22.5]
 
Example 2: 
Input: x,y,z = 6, 7, 5
Output: [14.696938456699069, 18, 9.0]
'''

# Solution:
def triangle(x,y,z):
  import math
  perimeter = x+y+z
  semiperi = (x+y+z)/2
  s = semiperi
  a = s*(s-x)*(s-y)*(s-z) ## Area using herons formula
  area = math.sqrt(a)
  l=[area, perimeter , semiperi]
  return l
  
print(triangle(x,y,z))

