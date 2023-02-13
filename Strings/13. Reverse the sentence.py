'''
Consider a sentence string as string1 consisting of some words. Reverse the order of words in the string and print the finalized reverse ordered string.

Example 1: 
Input: string1 = "apple boat crab"
Output: crab boat apple
 

Example 2: 
Input: string1 = "abc def ghi"
Output: ghi def abc

'''
# Solution:
def rev_sentence(string1):
  t = string1.split(" ")
  t1=t[::-1]
  s = ' '.join(t1)
  return s   
  
print(rev_sentence(string1))

# My Approach:
'''
string1 = "abc def ghi"

t = string1.split(" ")
t1=t[::-1]
# xs = ['1', '2', '3']
s = ' '.join(t1)
# var3 = " ".join([1, var2])
# for item in list:
#     s1
print(len(s))

'''
