"""
Q2. Implement Power Function

Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).
Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.


Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109


Input Format
Given three integers A, B, C.


Output Format
Return an integer.


Example Input
Input 1:
A = 2
B = 3
C = 3
Input 2:
A = 3
B = 3
C = 1


Example Output
Output 1:
2
Output 2:
0
"""
# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
sys.setrecursionlimit(200000)

def get_pow_val(A,B,C):
    if B == 0:
        return 1
    val = (A*A)%C
    fast_pow = get_pow_val(val,int(B/2),C)
    if B%2 == 0:
        return fast_pow
    else:

        return (A*fast_pow)%C


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        if A == 0:
            return 0
        return get_pow_val(A,B,C)