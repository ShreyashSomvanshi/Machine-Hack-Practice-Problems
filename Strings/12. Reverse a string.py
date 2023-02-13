'''
Consider a string as string1 consisting of N-number of characters. Reverse the string and print the finalized reversed string.

Example 1: 
Input: string1 = "abcd"
Output: dcba
 
Example 2: 
Input: string1 = "123+asw+171+wes"
Output: sew+171+wsa+321
'''

# Solution:

def string_reversing(string1):
  return string1[::-1]
  
print(string_reversing(string1))  


# My Approach:
'''
s = "abcd"
print(s[::-1])
'''
