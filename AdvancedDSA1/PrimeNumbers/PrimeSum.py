"""
Q1. Prime Sum

Problem Description
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.

If there is more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.



Problem Constraints
4 <= A <= 2*107



Input Format
First and only argument of input is an even number A.



Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.



Example Input
 4


Example Output
 [2, 2]


Example Explanation
 There is only 1 solution for A = 4.
"""
class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
        is_prime = [1]*(A+1)

        i = 2
        while i*i <= A:
            for k in range(i*i,A+1,i):
                is_prime[k] = i
            i += 1

        prime_set = set()
        prime_nums_list = []
        for i in range(2,A+1):
            if is_prime[i] == 1:
                prime_set.add(i)
                prime_nums_list.append(i)

        # print(prime_set)
        # print(prime_nums_list)
        for p1 in prime_nums_list:
            p2 = A - p1
            if p2 < 0:
                break
            if p2 in prime_set:
                return [p1,p2]


        return [1,1]