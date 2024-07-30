"""
Q2. Permutations

Problem Description
Given an integer array A of size N denoting collection of numbers , return all possible permutations.

NOTE:

No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Return the answer in any order
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. 
Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.


Problem Constraints
1 <= N <= 9



Input Format
Only argument is an integer array A of size N.



Output Format
Return a 2-D array denoting all possible permutation of the array.



Example Input
A = [1, 2, 3]


Example Output
[ [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3] 
  [2, 3, 1] 
  [3, 1, 2] 
  [3, 2, 1] ]


Example Explanation
All the possible permutation of array [1, 2, 3].
"""
def generate_permutations(res, cur_permutation,perm_len,A,n,remeining_elements):
    if perm_len == n:
        res.append(cur_permutation.copy())
        return
    else:
        current_elements = remeining_elements.copy()
        for num in current_elements:
            cur_permutation.append(num)
            remeining_elements.remove(num)
            generate_permutations(res, cur_permutation,perm_len+1,A,n,remeining_elements)
            cur_permutation.pop()
            remeining_elements.add(num)


class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
        res = []
        n = len(A)
        cur_permutation = []
        perm_len = 0
        remeining_elements = set(A)
        generate_permutations(res, cur_permutation,perm_len,A,n,remeining_elements)
        return res