"""
Q1. Sum of all Submatrices

Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.



Problem Constraints
1 <= N <=30

0 <= A[i][j] <= 10



Input Format
Single argument representing a 2-D array A of size N x N.



Output Format
Return an integer denoting the sum of all possible submatrices in the given matrix.



Example Input
Input 1:
A = [ [1, 1]
      [1, 1] ]
Input 2:
A = [ [1, 2]
      [3, 4] ]


Example Output
Output 1:
16
Output 2:
40
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        tot_sum = 0
        for i in range(n):
            for j in range(n):
                n_occurances = (i+1)*(n-i)*(j+1)*(n-j)
                tot_sum += (n_occurances*A[i][j])
        
        return tot_sum