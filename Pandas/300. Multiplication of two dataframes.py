'''
Consider two dictionaries as dict1 and dict2, consisting of the keys and their respective values. 
First, convert the dictionaries to two different data frames and then multiply these dataframes.

Example 1:
Input:
dict1 = {"X":[1,2,3,4,5],"Y":[2,4,6,7,8]}
dict2 = {"X":[2,3,4,5,6],"Y":[4,8,12,16,20]}
Output:
    X    Y
0   2    8
1   6   32
2  12   72
3  20  112
4  30  160

Example 2:
Input:
dict1 = {"X":[1,2,3,4,5],"Y":[2,3,4,5,6],"Z":[3,6,9,12,15]}
dict2 = {"X":[1,2,3,4,5],"Y":[2,3,4,5,6],"Z":[3,6,9,12,15]}
Output:
    X   Y    Z
0   1   4    9
1   4   9   36
2   9  16   81
3  16  25  144
4  25  36  225

Constraints: Assume that the two data frames have the same shape and column names.
'''

# Soln:
# 417 ms #1 leaderboard
import pandas as pd
def dataframe_multiplication(dict1,dict2):
  df1 = pd.DataFrame(dict1)
  df2 = pd.DataFrame(dict2)
  f = df1 * df2
  return f
  
print(dataframe_multiplication(dict1,dict2))

# 436 ms
# import pandas as pd  
# def dataframe_multiplication(dict1,dict2):
#   df1 = pd.DataFrame(dict1)
#   df2 = pd.DataFrame(dict2)
#   f = df1.mul(df2)
#   return f
  
# print(dataframe_multiplication(dict1,dict2))
