"""
Q4. Count Sort

Problem Description
Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.


Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 105


Input Format
The first argument is an integer array A.


Output Format
Return an integer array that is the sorted array A.


Example Input
Input 1:
A = [1, 3, 1]
Input 2:
A = [4, 2, 1, 3]


Example Output
Output 1:
[1, 1, 3]
Output 2:
[1, 2, 3, 4]


Example Explanation
For Input 1:
The array in sorted order is [1, 1, 3].
For Input 2:
The array in sorted order is [1, 2, 3, 4].
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_val = max(A)
        min_val = min(A)
        n = len(A)
        count_array = [0]*(max_val - min_val + 1)

        for num in A:
             count_array[num-min_val] += 1

        res = []
        for i in range(len(count_array)):
            val = min_val + i
            freq_count = count_array[i]
            while freq_count > 0:
                res.append(val)
                freq_count -=1

        return res