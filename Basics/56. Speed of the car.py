'''
A car covers a distance of K kilometres in a time period of T hours. Calculate the car's speed and return "Drive Slow " if the speed is more than or equal to 100 km/hr and return "Good Drive" if the car's speed is less than 100 km/hr.

Example 1:
Input:
K = 100
T = 0.36
Output: Drive Slow

Example 2:
Input:
K = 1000
T = 11
Output: Good Drive
'''

# Solution:

def speed(K,T):
  speed = K/T
  
  if speed >= 100:
    print("Drive Slow")
    
  else:
    print("Good Drive")
  
speed(K,T)
