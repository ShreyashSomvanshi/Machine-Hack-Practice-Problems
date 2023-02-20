# intermediate
'''

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
