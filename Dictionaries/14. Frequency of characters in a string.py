# intermediate
'''
Return a dictionary containing the frequency of each of the characters in a given string, string1.

Example 1: 
Input:  string1 = "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
 
Example 2: 
Input:  string1 = "blablabla"
Output: {'b': 3, 'l': 3, 'a': 3}
'''

# Solution:
def character_frequency(string1):
  all_freq = {}
 
  for i in string1:
    if i in all_freq:
      all_freq[i] += 1
    else:
      all_freq[i] = 1
      
  return all_freq
        
        
print(character_frequency(string1))

# Referred from:
# https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
