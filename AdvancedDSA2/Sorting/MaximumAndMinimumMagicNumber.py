"""
Q1. Maximum & Minimum Magic

Problem Description
Given an array of integers A of size N where N is even.

Divide the array into two subsets such that

1.Length of both subset is equal.
2.Each element of A occurs in exactly one of these subset.
Magic number = sum of absolute difference of corresponding elements of subset.

Note: You can reorder the position of elements within the subset to find the value of the magic number.

For Ex:- 
subset 1 = {1, 5, 1}, 
subset 2 = {1, 7, 11}
Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
Return an array B of size 2, where B[0] = maximum possible value of Magic number modulo 109 + 7, B[1] = minimum possible value of a Magic number modulo 109 + 7.



Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109

N is even



Input Format
The first argument given is the integer array A.



Output Format
Return an array B of size 2, where B[0] = maximum possible value of Magic number % 109 + 7,B[1] = minimum possible value of a Magic number % 109 + 7.



Example Input
Input 1:

 A = [3, 11, -1, 5]
Input 2:

 A = [2, 2]
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        # print(A)
        max_magic_num = 0
        min_magic_num = 0
        mod_val = 10**9 + 7

        i = 0;
        j = len(A) - 1
        while(i < j):
            max_magic_num = (max_magic_num + abs(A[i] - A[j])) % mod_val
            i += 1
            j -= 1


        for i in range(0,len(A)-1,2):
            min_magic_num = (min_magic_num + abs(A[i] - A[i+1])) % mod_val

        return [max_magic_num, min_magic_num]