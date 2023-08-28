'''
Check whether the given year Y is a leap year or not a leap year. 
Print Yes if the given year is a leap year, and print No if the given year is not a leap year.

Example 1:
Input:
Y = 2024
Output: Yes

Example 2:
Input:
Y = 1999
Output:cNo

Hints
A leap year has 366 days and can be divided by 4. Example 2004, 2012, 2020, etc.
'''

# Soln:
def leapYear(Y):
  if (Y%4 == 0):
    print('Yes')
  else:
    print('No')
    
leapYear(Y)

