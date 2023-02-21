# Advance
'''
Show whether a given integer N is an Armstrong number or not.

Example 1: 
Input:  N = 153
Output: Yes
 
Example 2: 
Input: N = 199
Output: No
'''

# Solution:
def armstrongNumber(N):
  number = str(N)

  N = len(number)
  output = 0
  for i in number:
      output = output+int(i)**N

  if output == int(number):
      return("Yes")
  else:
      return("No")

        
print(armstrongNumber(N))

# Referred from - https://www.geeksforgeeks.org/program-for-armstrong-numbers/
