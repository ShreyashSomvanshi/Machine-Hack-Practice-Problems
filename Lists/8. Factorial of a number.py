'''
Obtain the factorial of the given number N.

Example 1: 
Input:  N = 2
Output: 2
 
Example 2: 
Input:N = 5
Output: 120
'''

# Solutions: 



# Simplest solution:
def factorial(N):
  import math
  return math.factorial(N)
  
print(factorial(N))

# ===========================================================================================

# Other Approaches : referred from - https://www.programiz.com/python-programming/examples/factorial

# Using for loop:
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   
# ================================================================================================= 
  
 # using Recursion:
 # Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)
 
 
 
