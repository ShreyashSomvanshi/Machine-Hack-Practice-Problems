'''
You have to check whether the decimal representation of a given binary number is divisible by 5 or not.
Return Yes if divisible by 5 else, return No.

Example 1:
Input: bin = "101010"
Output: No

Example 2:
Input: bin = "1010"
Output: Yes

'''

# Solution:

class Solution:
  def isDivisibleBy5(self, Bin):
    g = int(Bin,2)
    if g%5 == 0:
      print("Yes")
      
    else:
      print("No")
      
k = Solution()
k.isDivisibleBy5(bin)

