'''
Consider two numbers, a and b. Return 1 if a < b, return 2 if a > b and return 3 if a = b.

Example 1:
Input:
a = 1234
b = 12345
Output: 1

Example 2:
Input:
a = 1723657863287
b = 1746871
Output: 2
'''
class Solution:
  def check(self, a,b):
    if a < b:
      return 1
    elif a > b:
      return 2
    elif a == b:
      return 3
  
sol = Solution()
print(sol.check(a,b))
      
    
