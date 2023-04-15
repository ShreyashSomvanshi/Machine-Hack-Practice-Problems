'''
Consider a list as input_list consisting of the integer elements. Obtain all the elements
in a new list which are greater than the average of elements in the main list.

Example 1:
Input: input_list = [1,2,3,4]
Output: [3, 4]

Example 2:
Input: input_list = [10,11,20,22,25]
Output: [20, 22, 25]

'''

# Solution:
def elements_greaterThan_average(list1):
  sum = 0
  for i in input_list:
    sum = sum+i
  u = sum/len(input_list)
  l=[]
  for i in range(len(input_list)):
    # print(input_list[i])
    if input_list[i]>u:
      l.append(input_list[i])
  return l
  
print(elements_greaterThan_average(input_list))
