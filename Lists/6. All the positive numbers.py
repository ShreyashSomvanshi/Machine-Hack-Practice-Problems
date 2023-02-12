'''
Obtain a list that contains positive integers within the range K to N. Assume N and K are also the integers.

Example 1: 
Input:  K = -9 ; N = 2
Output: [1, 2]
 
Example 2: 
Input: K = -100 ; N = 13
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''

# Solution:
def positiveNumber(K,N):
  l=[]  
  for i in range(K,N+1):
    if i>0:
      l.append(i)
    
  return l
    
print(positiveNumber(K,N))

# My approach:
'''
def positiveNumber(K,N):
    l=[]  
    for i in range(K,N):
        if i>0:
            l.append(i)
    
    return l
'''
