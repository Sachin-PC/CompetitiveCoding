"""
Q1. N integers containing only 1, 2 & 3

Problem Description
Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.

NOTE: All the A integers will fit in 32-bit integers.



Problem Constraints
1 <= A <= 29500



Input Format
The only argument given is integer A.



Output Format
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.



Example Input
Input 1:

 A = 3
Input 2:

 A = 7


Example Output
Output 1:

 [1, 2, 3]
Output 2:

 [1, 2, 3, 11, 12, 13, 21]


Example Explanation
Explanation 1:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2:

 Output denotes the first 7 integers that contains only digits 1, 2 and 3.
"""
import queue
import numpy as np

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        if A <= 3:
            return np.arange(1,A+1)
        perfect_numbers = queue.Queue()
        perfect_numbers.put(1)
        perfect_numbers.put(2)
        perfect_numbers.put(3)
        res = []
        res.append(1)
        res.append(2)
        res.append(3)
        count = 3
        while True:
            val = perfect_numbers.get()
            x = val*10 + 1
            y = val*10 + 2
            z = val*10 + 3
            perfect_numbers.put(x)
            res.append(x)
            if count + 1 == A:
                return res
            perfect_numbers.put(y)
            res.append(y)
            if count + 2 == A:
                return res
            perfect_numbers.put(z)
            res.append(z)
            if count + 3 == A:
                return res
            count += 3