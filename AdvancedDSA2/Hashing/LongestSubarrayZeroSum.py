"""
Q3. Longest Subarray Zero Sum

Problem Description
Given an array A of N integers.
Find the length of the longest subarray in the array which sums to zero.

If there is no subarray which sums to zero then return 0.



Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109


Input Format
Single argument which is an integer array A.


Output Format
Return an integer.


Example Input
Input 1:

 A = [1, -2, 1, 2]
Input 2:

 A = [3, 2, -1]


Example Output
Output 1:

3
Output 2:

0


Example Explanation
Explanation 1:

 [1, -2, 1] is the largest subarray which sums up to 0.
Explanation 2:

 No subarray sums up to 0.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        arr_sum = 0
        sum_map = {}

        best_diff = 0
        for i in range(1,len(A)):
            A[i] = A[i] + A[i-1]
            if A[i] == 0:
                if i+1 > best_diff:
                    best_diff = i+1
            elif A[i] in sum_map:
                sum_map[A[i]][1] = i
                if (i - sum_map[A[i]][0]) > best_diff:
                    best_diff = i - sum_map[A[i]][0]
            else:
                sum_map[A[i]] = [i,-1] 

        return best_diff