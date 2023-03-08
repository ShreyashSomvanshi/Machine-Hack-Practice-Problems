'''
Find the number of white spaces between each word in a string given as string1 consisting of n-number of characters.

Example 1:
Input: string1 = "a b"
Output: 1

Example 2:
Input: string1 = "a b c d e f g"
Output: 6
'''

# Solution:
def whiteSpaces(string1):
  u=string1.split(' ')
  y=len(u)
  return y-1  

print(whiteSpaces(string1))


