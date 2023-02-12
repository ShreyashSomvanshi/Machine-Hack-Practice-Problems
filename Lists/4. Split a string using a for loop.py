'''
Intermediate:

Consider a list as list1 containing N-number of strings.
Split the given string into two separate lists with respect to the white spaces between them and print them as a list of lists.

Example 1: 
Input: list1 =["a A","b B","c C"]
Output: [['a', 'b', 'c'], ['A', 'B', 'C']]

Example 2: 
Input: list1 =["sp 17","ak 17","leo 10"]
Output: [['sp', 'ak', 'leo'], ['17', '17', '10']]

'''

# Solution:







# My approach:
'''
def splitting_string(list1):
    for i in range(len(list1)):
        listt = list1[i].split(' ')
        list2=[]
        list3=[]
        list2.append(listt[0])
        list3.append(listt[1])
        del listt[:]
        list4=[]
        list4.append(list2[i])
        list4.append(list3[i])
        print(list4)
        i=i+1
        # print("listt is ", listt)
        #       listt=list1[i]
        #       listt.split(' ')
        #       return listt
  
  
  
list1 =["a A","b B","c C"]


print(splitting_string(list1))


# listt = list1[1].split(' ')
# list2=[]
# list3=[]
# list2.append(listt[0])
# list3.append(listt[1])
# del listt[:]
# list4=[]
# list4.append(list2[i])
# list4.append(list3[i])
# print(list4)
# print("listt is ", listt)
# list
# print(len(list1))
# print(splitting_string(list1))

# Output:

# [['a', 'b', 'c'], ['A', 'B', 'C']]

'''
