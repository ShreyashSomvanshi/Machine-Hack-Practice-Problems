'''
Consider a tuple as tuple1 made up of three items such as ( a, b, c ) provided a,b and c can be any datatype.
Iterate through the items inside the tuple based on their index number using a for-loop and print the values.

Example 1: 
Input: tuple1 = (11.11,"ak17", 17)
Output: 
11.11
ak17
17
 

Example 2: 
Input:  tuple1 = (1997,1998,1999)
Output: 
1997
1998
1999

'''

# Solution:

def tuplee(tuple1):
  for i in range(len(tuple1)):
    print(tuple1[i])

tuplee(tuple1)
