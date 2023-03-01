'''
Create a dataframe consisting of the keys and their respective values. Once created, remove the 
N-th column from the dataframe and show the final dataframe.

Example 1:
Input:
dict1 = {"a":[5,17,96],
        "b":[17,85,17],
        "c" :[14,7,17]}
N = 3

Output:
    a   b
0   5  17
1  17  85
2  96  17


Example 2:
Input:
dict1 = {"csk":[205,177,196],
        "rcb":[147,185,175],
        "rr" :[134,97,147],
        "mi" :[142,148,178],
        "kkr" :[147,169,120],
        "kxip":[119,120,163]}
N = 2

Output:
    csk   rr   mi  kkr  kxip
0  205  134  142  147   119
1  177   97  148  169   120
2  196  147  178  120   163

'''

# Solution:

import pandas as pd
def dropping_column(dict1,N):
  df = pd.DataFrame(dict1)
  df.drop(df.columns[[N-1]], axis=1, inplace=True)
  return df
  
print(dropping_column(dict1,N))
  

