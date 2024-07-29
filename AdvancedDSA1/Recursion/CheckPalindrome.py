"""
Q3. Check Palindrome using Recursion

Problem Description
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.



Problem Constraints
1 <= |A| <= 50000

String A consists only of lowercase letters.



Input Format
The first and only argument is a string A.



Output Format
Return 1 if the string A is a palindrome, else return 0.



Example Input
Input 1:

 A = "naman"
Input 2:

 A = "strings"


Example Output
Output 1:

 1
Output 2:

 0
"""
def check_palindrome(A,i,j):
    if i >= j:
        return 1
    else:
        if A[i] != A[j]:
            return 0
        else:
            return check_palindrome(A,i+1,j-1)

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        i = 0
        j = n-1
        sys.setrecursionlimit(int(n/2)+10)
        res = check_palindrome(A,i,j)

        return res