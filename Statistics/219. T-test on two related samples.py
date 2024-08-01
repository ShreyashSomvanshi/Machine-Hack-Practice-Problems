'''
Consider two related samples as sample1 and sample2. Perform the t-test on the two related 
samples having identical average values and return the t-statistic value and p-value as output.

Example 1:
Input:
sample1 =[30,68,77,119,35,11,33,30,29,62,39]
sample2=[31,62,97,101,25,16,25,36,27,61,31]

Output:
Ttest_relResult(statistic=0.6285059317130549, pvalue=0.5437600392053596)

Example 2:
Input:
sample1 =[6,2,3,4,2,3,3,2,7,8]
sample2=[5,31,43,48,50,41,71,919,393,1]

Output:
Ttest_relResult(statistic=-1.7012469386594702, pvalue=0.12310741290091204)

Hints
T-test on the two related samples is a test for the null hypothesis that two related 
or repeated samples have identical average (expected) values.
'''

# Soln:

from scipy.stats import ttest_rel

def TWO_RELATED_samples(sample1,sample2):
  t_statistic, p_value = ttest_rel(sample1, sample2)
  print("Ttest_relResult(statistic={}, pvalue={})".format(t_statistic, p_value))

TWO_RELATED_samples(sample1,sample2)
