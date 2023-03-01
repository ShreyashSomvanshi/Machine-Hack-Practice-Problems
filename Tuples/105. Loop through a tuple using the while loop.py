'''
Consider a tuple as tuple1 made up of three items such as ( a, b, c ) provided a,b and c can be any datatype.
Write a python program to Iterate through the items inside the tuple based on their index number using a while-loop and print the values.

Example 1:
Input: tuple1 = (11.11,"ak17", 17)
Output:
11.11
ak17
17

Example 2:
Input: tuple1 = (1997,1998,1999)
Output:
1997
1998
1999

'''

# Solution:

def loop(t):
  for i in t:
    print(i)
    
loop(tuple1)
