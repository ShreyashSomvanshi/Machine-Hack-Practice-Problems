'''
Consider three strings as s1, s2, and s3. Concatenate all the three strings with a white space between them and find the length of the concatenated string.
Finally, print both the concatenated string and the length of the concatenated string in a single list.

Example 1:
Input:  s1 = "abc" s2 = "efg" s3 = "hij"
Output: ['abc efg hij', 11]
 
Example 2: 
Input: s1 = "Practice" s2 = "With" s3 = "MachineHack"
Output: ['Practice With MachineHack', 25]

'''

# Solution:

def concatenate(string1,string2,string3):
  var3 = " ".join([s1, s2, s3])
  g = len(var3)
  # print(var3)
  l = []
  l.append(var3)
  l.append(g)
  return l
  
print(concatenate(s1,s2,s3))


# My Approach
'''
s1 = "abc"
s2 = "efg"
s3 = "hij"
var3 = " ".join([s1, s2, s3])
g = len(var3)
# print(var3)
l = []
l.append(var3)
l.append(g)
# s = s1,s2,s3
print(l)
# Output: 

# ['abc efg hij', 11]

'''
