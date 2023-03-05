'''
Rearrange the words of a given string string1 in alphabetical order.

Example 1:
Input: string1 = "zebra cat mouse apple bat goat dog elephant fox "
Output: apple bat cat dog elephant fox goat mouse zebra

Example 2:
Input: string1 = "india is the wettest inhabited place on earth"
Output: earth india inhabited is on place the wettest
'''

# Solution:
def rearrangeString(string1):
  list_words = string1.strip().split(" ")
    
  for i in range(len(list_words)):
    list_words[i] = list_words[i].lower()
       
  result = sorted(list_words)
  print(' '.join(result))
    
rearrangeString(string1)






