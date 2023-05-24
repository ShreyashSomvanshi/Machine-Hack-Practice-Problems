'''
You are given a list of ground truth labels y_true_list and a list of predicted labels y_pred_list for multiple classes.
Write a function that takes these two lists as input and returns a pandas DataFrame containing evaluation metrics for each class.
The function should calculate the ROC AUC score, precision, and recall for each class. The input lists may contain multiple elements,
each corresponding to a different class. The function should return a DataFrame with one row per class and three columns containing the
evaluation metrics.

Example 1:

Input:
y_true_list = [[0, 1, 1, 0, 1],
[1, 1, 0, 0],
[0, 0, 1, 1, 0, 1]]
y_pred_list = [[0, 1, 0, 0, 1],
[1, 1, 1, 0],
[0, 0, 1, 0, 1, 1]]

Output:

ROC AUC Score Precision Recall
0 0.833333 0.866667 0.800000
1 0.750000 0.833333 0.750000
2 0.666667 0.666667 0.666667

Example 2:

Input:

y_true_list = [[1, 0, 0, 1, 1],
[0, 1, 0, 1],
[1, 1, 0, 0, 1, 0]]
y_pred_list = [[1, 0, 1, 1, 1],
[0, 1, 0, 0],
[1, 0, 0, 1, 1, 1]]
Output:

ROC AUC Score Precision Recall
0 0.75 0.850000 0.80
1 0.75 0.833333 0.75
2 0.50 0.500000 0.50

Constraints: The output should be in the pandas DataFrame.

'''

# Solution:
  
  
  
  
  
  
  
  
  
