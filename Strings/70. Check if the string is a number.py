'''
Consider a string as string1. Use the try-except method to print YES if the given string is numeric and print NO if the given string is non-numeric.

Example 1:
Input: string1 = "123.23"
Output: YES

Example 2:
Input:
string1 = "alpha000"
Output: NO

'''

# Solution:
def isnumeric(string1):
  try:
    g=float(string1)
    u = int(g)
    if type(u)==int:
      print("YES")
  except ValueError:
    print("NO")    
    
isnumeric(string1)
  


