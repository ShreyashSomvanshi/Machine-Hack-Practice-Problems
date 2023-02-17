# Intermediate
'''
Consider a list as listIn consisting of the elements of three different data types such as integer, float, and string. Separate all the elements based on their data types into different lists and print them all together as a list of lists in the specific order of [[integer], [float], [string]]. 

Example 1: 
Input:  listIn = [1,"a",17.2]
Output: [[1], [17.2], ['a']]
 
Example 2: 
Input: listIn = [1,2,"a","b",1.2,2.1]
Output: [[1, 2], [1.2, 2.1], ['a', 'b']]
'''

# Solution:
def splittingDatatypes(listIn):
  intt = []
  floatt = []
  strr = []
  
  l=[]
  
  for i in listIn:
    
    if type(i) == int:
      intt.append(i)
    elif type(i) == str:
      strr.append(i)
    elif type(i) == float:
      floatt.append(i)
    else:
      print("Invalid Data entered!!")
  l.append(intt)
  l.append(floatt)
  l.append(strr)
  return l
  
print(splittingDatatypes(listIn))


# My Approach:
'''
listIn = [1,2,"a","b",1.2,2.1]
# Output:

#  [[1, 2], [1.2, 2.1], ['a', 'b']]
intt = []
floatt = []
strr = []

l=[]

for i in listIn:
    if type(i) == int:
        intt.append(i)
    elif type(i) == str:
        strr.append(i)
    else:
        floatt.append(i)
l.append(intt)
l.append(floatt)
l.append(strr)

print('int lst: ', intt)
print('float lst: ', floatt)
print('str lst: ', strr)
print(l)
# a = 45.2
# print(type(a)==float)
'''
