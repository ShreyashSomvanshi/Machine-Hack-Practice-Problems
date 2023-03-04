'''
Check whether a given string string1 is a palindrome or not. Print YES if the string is a palindrome, and print NO if the string is not a palindrome.

Example 1:
Input: string1 = "palindrome"
Output: NO

Example 2:
Input: string1 = "racecar"
Output: YES

'''

# Solution:
def palindrome(string1):
  o=string1[::-1]
  if string1 == o:
    print("YES")
  else:
    print("NO")
    
palindrome(string1)
    
