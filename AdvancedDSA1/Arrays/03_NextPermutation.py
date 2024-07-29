"""
Q1. Next Permutation

Problem Description
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order, i.e., sorted in ascending order.

NOTE:

The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.


Problem Constraints
1 <= N <= 5 * 105

1 <= A[i] <= 109



Input Format
The first and the only argument of input has an array of integers, A.



Output Format
Return an array of integers, representing the next permutation of the given array.



Example Input
Input 1:

 A = [1, 2, 3]
Input 2:

 A = [3, 2, 1]


Example Output
Output 1:

 [1, 3, 2]
Output 2:

 [1, 2, 3]
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n = len(A)
        num = A[n-1]
        sort_start_index = 0
        sort_end_index = n
        for i in range(n-2,-1,-1):
            if A[i] < num:
                num_considered = num
                num_considered_index = i+1
                for j in range(i+2,n):
                    if A[i] < A[j]:
                        num_considered = A[j]
                        num_considered_index = j
                    else:
                        break
                temp = A[i]
                A[i] = A[num_considered_index]
                A[num_considered_index] = temp
                sort_start_index = i+1
                break
            else:
                num = A[i]
        
        A[sort_start_index:sort_end_index] = sorted(A[sort_start_index:sort_end_index])

        return A
            