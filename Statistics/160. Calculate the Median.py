'''
Find the median of the given data data1 containing weights of different persons.

Example 1:
Input: data1 = [45,46,47,48]
Output: 46.5

Example 2:
Input: data1 = [95,46,90,99,53]
Output: 90
'''

# Short Solution:
import statistics
  
def mediann(data1):  
  return statistics.median(data1)

print(mediann(data1))

# =============================== OR ====================================

# My Solution:
def median(data1):  
# First sort in ascending order; Median = {(n + 1) / 2}th value for n=even,
# Median = n/2 for n=odd but adjust by -1 as indices start with 0
  j = sorted(data1)
  length = len(j)
  if (length % 2) == 0:
    med = int((length/2))
    med2 = int((length/2)-1)
    d = j[med]
    o = j[med2]
    g = []
    g.append(d)
    g.append(o)
    avg = sum(g)/2
    
  else:
    g = int((length+1)/2)
    avg = j[g-1]
    
  return avg

print(median(data1))



# My Approach:

'''
def median(data1):  # First sort in ascending order; Median = {(n + 1) / 2}th value for n=even, Median = n/2 for n=odd
  j = sorted(data1)
  length = len(j)
  if (length % 2) == 0:
    med = int((length/2))
    med2 = int((length/2)-1)
    d = j[med]
    print(d)
    o = j[med2]
    g = []
    g.append(d)
    g.append(o)
    print(g)
    avg = sum(g)/2
    
    
  else:
    avg = (length+1)/2
    
#   med = int(med)
  return avg
  
data1 = [45,46,47,48]
# Output:

# 46.5
# j = sorted(data1)
print(median(data1))

'''
