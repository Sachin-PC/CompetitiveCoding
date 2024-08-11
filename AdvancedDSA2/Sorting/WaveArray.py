"""
Q2. Wave Array

Problem Description
Given an array of integers A, sort the array into a wave-like array and return it.
In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5..... 
NOTE: If multiple answers are possible, return the lexicographically smallest one.



Problem Constraints
1 <= len(A) <= 106
0 <= A[i] <= 106



Input Format
The first argument is an integer array A.



Output Format
Return an array arranged in the sequence as described.



Example Input
Input 1:

A = [1, 2, 3, 4]
Input 2:

A = [1, 2]


Example Output
Output 1:

[2, 1, 4, 3]
Output 2:

[2, 1]


Example Explanation
Explanation 1:

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
First answer is lexicographically smallest. So, return [2, 1, 4, 3].
Explanation 1:

Only possible answer is [2, 1].
"""
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
        A.sort()
        res = []
        i = 1
        j = len(A)-1
        n=0
        a_len = len(A)
        while n < len(A):
            if i < a_len:
                res.append(A[i])
            res.append(A[i-1])
            i += 2
            # j -= 1
            n += 2
        return res