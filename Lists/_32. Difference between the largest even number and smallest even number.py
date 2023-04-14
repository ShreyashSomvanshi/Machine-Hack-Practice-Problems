'''
Create a list as list1 containing all the even numbers in the range between N to K. 
Obtain the difference between the largest even number and smallest even number in the list.

Example 1:
Input:
N = 1
K = 10
Output: 8

Example 2:
Input:
N = 100
K = 221
Output: 120

'''

# Solution:

def difference(N,K):
  evn = []
  for i in range(N,K+1):
    if i%2 == 0:
      evn.append(i)
  diff = evn[-1] - evn[0]
  return diff
  
print(difference(N,K))


# ++++++++++ OR ++++++++++++++

def difference(N,K):
 result=[i for i in range(N,K+1) if i%2==0]
 return max(result)-min(result)

print(difference(N,K))

