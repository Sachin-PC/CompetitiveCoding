"""
Q3. Subset
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given a set of distinct integers A, return all possible subsets.

NOTE:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The initial list is not necessarily sorted.


Problem Constraints
1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format
First and only argument of input contains a single integer array A.



Output Format
Return a vector of vectors denoting the answer.



Example Input
Input 1:

A = [1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

[
    []
    [1]
]
Output 2:

[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]
"""
def get_subsets(A,res,cur_subset,n,cur_index):
    if cur_index == n:
        return
    else:
        cur_subset.append(A[cur_index])
        res.append(cur_subset.copy())
        get_subsets(A,res,cur_subset,n,cur_index+1)
        cur_subset.pop()
        get_subsets(A,res,cur_subset,n,cur_index+1)

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsets(self, A):
        A.sort()
        res = []
        n = len(A)
        cur_subset = []
        cur_index = 0
        res.append([])
        get_subsets(A,res,cur_subset,n,cur_index)
        return res