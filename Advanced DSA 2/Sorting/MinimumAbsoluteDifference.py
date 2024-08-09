"""
Q2. Minimum Absolute Difference

Problem Description
Given an array of integers A, find and return the minimum value of | A [ i ] - A [ j ] | where i != j and |x| denotes the absolute value of x.



Problem Constraints
2 <= length of the array <= 100000

-109 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the minimum value of | A[i] - A[j] |.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 1
Output 2:

 6
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        min_diff = float('inf')
        for i in range(len(A)-1):
            if abs(A[i] - A[i+1]) < min_diff:
                min_diff = abs(A[i] - A[i+1])
        
        return min_diff