'''
Consider the given sales price as S and the actual price as A. Based on these given values, check whether 
profit has been made or loss has been incurred.

Example 1: 
Input:  A,S = 500,100
Output: Loss 400
 
Example 2: 
Input: A,S = 500,600
Output: Profit 100
'''

# My Solution:

#Write the code here
def profitLoss(A,S):
  if S>A:
    print('Profit', abs(S-A))
    
  else:
    print('Loss', abs(S-A))
  
profitLoss(A,S)
