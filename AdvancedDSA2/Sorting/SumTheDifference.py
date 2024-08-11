"""
Q1. Sum the Difference

Problem Description
Given an integer array, A of size N.
You have to find all possible non-empty subsequences of the array of numbers and then,
for each subsequence, find the difference between the largest and smallest number in that subsequence.
Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.



Problem Constraints
1 <= N <= 10000

1<= A[i] <=1000



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the output.



Example Input
Input 1:

A = [1, 2] 
Input 2:

A = [3, 5, 10]


Example Output
Output 1:

 1 
Output 2:

 21


Example Explanation
Explanation 1:

All possible non-empty subsets are:
[1]     largest-smallest = 1 - 1 = 0
[2]     largest-smallest = 2 - 2 = 0
[1, 2]  largest-smallest = 2 - 1 = 1
Sum of the differences = 0 + 0 + 1 = 1
So, the resultant number is 1 
Explanation 2:

All possible non-empty subsets are:
[3]         largest-smallest = 3 - 3 = 0
[5]         largest-smallest = 5 - 5 = 0
[10]        largest-smallest = 10 - 10 = 0
[3, 5]      largest-smallest = 5 - 3 = 2
[3, 10]     largest-smallest = 10 - 3 = 7
[5, 10]     largest-smallest = 10 - 5 = 5
[3, 5, 10]  largest-smallest = 10 - 3 = 7
Sum of the differences = 0 + 0 + 0 + 2 + 7 + 5 + 7 = 21
So, the resultant number is 21 
"""
def get_pow(a,i,mod_val):
    if i == 0:
        return 1
    else:
        x = get_pow(a,int(i/2),mod_val)
        res = (x*x)%mod_val
        if i%2 == 0:
            return res
        else:
            return (res*2)%mod_val

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        mod_val = 10**9 + 7
        A.sort()

        n = len(A)
        res = 0
        for i in range(n):
            max_in_subsets = get_pow(2,i,mod_val)
            min_in_subsets = get_pow(2,n-i-1,mod_val)

            res = (res + (A[i]*(max_in_subsets - min_in_subsets))%mod_val)%mod_val

        return res