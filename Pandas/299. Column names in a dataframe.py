'''
Create a dataframe from a given dictionary dict1 consisting of keys and 
respective values and then obtain the names of all the columns of the dataframe,

Example 1:
Input:
dict1 = {"Name":["X","Y"],
        "Age":[23,23],
        "Number":[17,23],
        "Team":["RMF","RMF"],
        "Position":["CMF","LF"]}
Output: ['Name', 'Age', 'Number', 'Team', 'Position']

Example 2:
Input:
dict1 = {"Name":["Aswin","Selvin"],
        "Class":["12th","12th"],
        "Mark":[405,450],
        "Rank":["5th","2th"]}
Output: ['Name', 'Class', 'Mark', 'Rank']
'''

# Soln:

import pandas as pd
def column_names(dict1):
  df = pd.DataFrame(dict1)
  return list(df.columns)

print(column_names(dict1))
