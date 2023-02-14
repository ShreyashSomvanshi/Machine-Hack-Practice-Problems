'''
Calculate the simple interest of the given principal (P), rate of interest (R) per annum, and time period (T). 

Example 1: 
Input:  P,R,T = 2000,10,7
Output: 1400.0
 

Example 2: 
Input: P,R,T = 10000,3,2.5
Output: 750.0
'''

# Solution:
def simpleInterest(P,R,T):
  return (P*R*T/100)
  
print(simpleInterest(P,R,T))

