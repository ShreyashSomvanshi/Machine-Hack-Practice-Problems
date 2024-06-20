'''
Consider a list as list1 consisting of the integer elements. Group the list 
elements into equally sized buckets possible, consider bucket size as B and 
show the resultant list.

Example 1:
Input: list1 = [1,2,3,4,5,6] ; B = 3
Output: [[1, 2, 3], [4, 5, 6]]

Example 2:
Input: list1 = [1,5,6,2,9,2,7] ; B = 2
Output: [[1, 5], [6, 2], [9, 2], [7]]
'''

# Soln:

def split_list_into_buckets(input_list, bucket_size):
    return [input_list[i:i + bucket_size] for i in range(0, len(input_list), bucket_size)]

output = split_list_into_buckets(list1, B)
print(output)
