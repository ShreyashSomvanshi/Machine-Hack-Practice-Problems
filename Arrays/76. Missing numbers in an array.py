'''
Consider a sorted array as array1 containing multiple missing elements, i.e. consider an array 
as [ a, b, d, f ] and the corresponding missing values are [ c, e ] provided a,b,c,d,e, and f are
integers. Obtain all the missing elements present in the range of minimum and maximum elements in the array.

Example 1:
Input: array1 = [1,3]
Output: [2]

Example 2:
Input: array1 = [1,2,3,6,7]
Output: [4, 5]
'''

# Solution: By ChatGPT

def MissingElements(array1):
    missing_elements = []
    for i in range(len(array1)-1):
        diff = array1[i+1] - array1[i]
        if diff > 1:
            for j in range(1, diff):
                missing_elements.append(array1[i]+j)
    return missing_elements


  
print(MissingElements(array1))
    

# My approach:

def MissingElements(array):
    l=[]
    for i in range(len(array)):
        if array[i] != i+1:
            l.append(i+1)
        
    return l    
# # array1 = [1,2,3,6,7]
# # Output:
array1 = [1,2,3,5,6]
# [4, 5]      
print(MissingElements(array1))
         


      
