'''
Considering an array “arr” of integers, return the Kth smallest element from the list.

Example 1:
Input:
arr = [7, 10, 4, 3, 20, 15]
K = 3
Output: 7

Example 2:
Input:
arr = [7, 10, 4, 3, 20, 15, 65, 87, 34, 65, 87, 34, 65, 86, 38]
K = 7
Output: 34
'''

# Accepted Soln:
def kthSmallest(arr, K):
    f = sorted(arr)
    return f[K-1]

print(kthSmallest(arr,K))



# Soln: Correct but didn't get accepted
class Solution:
  def kthSmallest(self,arr, K):
    f = sorted(arr)
    print(f)
    return f[K-1]

sol = Solution()
sol.kthSmallest(arr,K)
