"""
Q2. Find Fibonacci - II

Problem Description
The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

Given a number A, find and return the Ath Fibonacci Number using recursion.

Given that F0 = 0 and F1 = 1.



Problem Constraints
0 <= A <= 20



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the Ath term of the sequence.
"""
def getFibonacciNumber(A,f_n2,f_n1,n):
    f_n = f_n2 + f_n1
    if n == A:
        return f_n
    else:
        return getFibonacciNumber(A,f_n1,f_n,n+1)
class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):

        if A == 0:
            return 0
        elif A == 1:
            return 1
        f_n2 = 0
        f_n1 = 1
        return getFibonacciNumber(A,f_n2,f_n1,2)