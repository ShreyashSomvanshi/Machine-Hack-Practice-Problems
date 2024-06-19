'''
Consider a list, list1, consisting of the integer elements. Obtain all the 
even elements in the given list, excluding those elements which are the 
multiples of K, given that K is an integer.

Example 1:
Input:
list1 = [1,2,3,4,5,6,7,8,9,10]; K = 4
Output: [2, 6, 10]

Example 2:
Input:
list1 = [2,4,6,7,8,1,10,12,14,15]; K = 3
Output: [2, 4, 8, 10, 14]
'''
# Soln:
def evenExpectN(list1,K):
  u = []
  for i in list1:
    if i%2 == 0:
      if i%K != 0:
        u.append(i)
  return u
  
print(evenExpectN(list1,K))


# Soln2:
def evenExpectN(list1,K):
    return [num for num in list1 if num % 2 == 0 and num % K != 0]

print(evenExpectN(list1,K))

# Soln3:
def filter_even_not_divisible_by_K(list1, K):
    return (num for num in list1 if num % 2 == 0 and num % K != 0)

print(list(filter_even_not_divisible_by_K(list1, K)))
