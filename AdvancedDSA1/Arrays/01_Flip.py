"""
Q2. Flip

Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.



Problem Constraints
1 <= size of string <= 100000



Input Format
First and only argument is a string A.



Output Format
Return an array of integers denoting the answer.



Example Input
Input 1:

A = "010"
Input 2:

A = "111"


Example Output
Output 1:

[1, 1]
Output 2:

[]


Example Explanation
Explanation 1:

A = "010"

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Explanation 2:

No operation can give us more than three 1s in final string. So, we return empty array [].
"""

import numpy as np

def get_max_sum_subarray(A):
    n = len(A)
    cur_sum = 0
    max_sum = 0
    best_start_index = 0
    best_end_index = -1
    start_index = 0
    flag = 1
    for i in range(n):
        cur_sum += A[i]
        if flag == 1 and cur_sum >=0:
            start_index = i
            flag = 0
        if cur_sum > max_sum:
            best_start_index = start_index
            best_end_index = i
            max_sum = cur_sum
        elif cur_sum < 0:
            cur_sum = 0
            flag = 1
    if max_sum == 0:
        return []
    else:
        return [best_start_index+1,best_end_index+1]


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        bin_arr = np.zeros(n, dtype = int)
        original_one_count = 0
        for i in range(n):
            if A[i] == '0':
                bin_arr[i] = 1
            else:
                original_one_count += 1
                bin_arr[i] = -1
        
        res = get_max_sum_subarray(bin_arr)
        return res
        # for i in range(best_start_index,best_end_index+1):
        #     bin_arr[i] = bin_arr[i]*-1
        
        # flipped_one_count = 0
        # for i in range(n):
        #     if bin_arr[i] == -1:
        #         flipped_one_count += 1
        # # flipped_one_count = bin_arr.count(-1)

        # if flipped_one_count > original_one_count:
        #     return [best_start_index+1,best_end_index+1]
        # else:
        #     return []
