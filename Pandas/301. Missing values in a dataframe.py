'''
Consider two dictionaries dict1 and dict2, consisting of the keys and their respective values. 
First, convert the dictionaries to two different data frames and the fill all the missing values 
present in the data frame with a given numerical value, N. Finally, find the multiplication of 
the two data frames.

Example 1:
Input:
dict1 = {"X":[1,2,None],"Y":[2,4,6]}
dict2 = {"X":[2,None,6],"Y":[4,8,20]}
N = 10

Output:
      X    Y
0   2.0    8
1  20.0   32
2  60.0  120


Example 2:
Input:
dict1 = {"X":[1,2,3,None,5],"Y":[21,3,4,5,6],"Z":[3,4,9,None,5]}
dict2 = {"X":[10,8,4,4,5],"Y":[2,31,4,5,None],"Z":[4,6,9,5,5]}
N = 5

Output:

      X     Y     Z
0  10.0  42.0  12.0
1  16.0  93.0  24.0
2  12.0  16.0  81.0
3  20.0  25.0  25.0
4  25.0  30.0  25.0


Constraints: Assume that the two data frames have the same shape and column names.

Hints: Use mul() function to multiply pandas dataframes.
'''

# Solution: 479ms #1 leaderboard

import pandas as pd
def dataframe_multiplication(dict1,dict2,N):
    df1 = pd.DataFrame(dict1).fillna(N)
    df2 = pd.DataFrame(dict2).fillna(N)
    f = df1*df2
    return f

print(dataframe_multiplication(dict1,dict2,N))



## OR ## 492 ms

import pandas as pd
def dataframe_multiplication(dict1,dict2,N):
    df1 = pd.DataFrame(dict1).fillna(N)
    df2 = pd.DataFrame(dict2).fillna(N)
    f = df1.mul(df2)
    return f
  
