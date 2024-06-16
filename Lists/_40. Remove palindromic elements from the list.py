'''
Consider a list of lists as list1 consisting of the integer elements. 
Remove all the elements from the list with palindrome equivalent elements and print the resultant list.

Example 1:
Input: list1 = [39,93,27,72,51,42]
Output: [51, 42]

Example 2:
Input: list1 = [12,17,21]
Output: [17]
'''

## Soln:
def remove_palindromeElements(list1):
  t = []
  for i in list1:
    if int(str(i)[::-1]) in list1:
      pass
    else:
      t.append(i)
  return t
 
print(remove_palindromeElements(list1))
