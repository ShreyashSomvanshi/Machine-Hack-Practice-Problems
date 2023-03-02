'''
Consider a list as list1 consisting of the integer elements. Obtain all the elements present at the odd index positions of the list.

Example 1:
Input: list1 = [0,1,2,3]
Output: [1, 3]

Example 2:
Input: list1 = [100,123,111,99,"JD",12.2]
Output: [123, 99, 12.2]
'''

# Solution:

def oddIndexElements(list1):
    k=[]
    for i in range(len(list1)):
        if i%2!=0:
            k.append(list1[i])
    return k

      
print(oddIndexElements(list1))
  
 
