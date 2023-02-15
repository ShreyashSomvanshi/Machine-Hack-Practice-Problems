'''
Consider a string as string1 consisting of N-number of characters. Group all the even-length words and odd-length words separately as a list of lists. 

Example 1: 
Input: string1 = "a ab abc abcd abcde abcdef"
Output: [['ab', 'abcd', 'abcdef'], ['a', 'abc', 'abcde']]
 

Example 2: 
Input:  string1 = "12 123 1234 12345"
Output: [['12', '1234'], ['123', '12345']]
'''

## Solution:
def even_odd_length_string(string1):
  even=[]
  odd=[]
  st = string1.split(' ')
  for i in st:
      if len(i)%2 == 0:
          even.append(i)
      else:
          odd.append(i)
  l=[]
  l.append(even)
  l.append(odd)
  return l
  
  
print(even_odd_length_string(string1))
