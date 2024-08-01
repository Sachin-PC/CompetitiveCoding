"""
Q3. Find All Primes
Problem Description
Given an integer A. Find the list of all prime numbers in the range [1, A].


Problem Constraints
1 <= A <= 106



Input Format
Only argument A is an integer.



Output Format
Return a sorted array of prime number in the range [1, A].



Example Input
Input 1:
A = 7
Input 2:
A = 12


Example Output
Output 1:
[2, 3, 5, 7]
Output 2:
[2, 3, 5, 7, 11]


Example Explanation
For Input 1:
The prime numbers from 1 to 7 are 2, 3, 5 and 7.
For Input 2:
The prime numbers from 1 to 12 are 2, 3, 5, 7 and 11.
"""
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        is_prime = [1]*(A+1)
        i = 2
        res = []
        while i*i<=A:
            # print("i = ",i)
            for k in range(i*i,A+1,i):
                is_prime[k] = 0
            i += 1
        
        for i in range(2,len(is_prime)):
            if is_prime[i] == 1:
                res.append(i)
        return res
