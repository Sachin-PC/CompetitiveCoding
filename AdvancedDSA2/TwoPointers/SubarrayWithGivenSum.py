"""
Q1. Subarray with given sum

Problem Description
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

If the answer does not exist return an array with a single integer "-1".

First sub-array means the sub-array for which starting index in minimum.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format
The first argument given is the integer array A.

The second argument given is integer B.



Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single integer "-1".



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:

 A = [5, 10, 20, 100, 105]
 B = 110


Example Output
Output 1:

 [2, 3]
Output 2:

 [-1]


Example Explanation
Explanation 1:

 [2, 3] sums up to 5.
Explanation 2:

 No subarray sums up to required number.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        start_index = 0
        end_index=-1
        continuous_sum = 0
        for index in range(n):
            continuous_sum += A[index]
            while continuous_sum > B:
                continuous_sum -= A[start_index]
                start_index += 1
            if continuous_sum == B:
                end_index = index
                break
        
        if end_index == -1:
            return [-1]
        else:
            res = []
            for i in range(start_index, end_index+1):
                res.append(A[i])

            return res