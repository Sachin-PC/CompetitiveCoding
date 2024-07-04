"""
Q1. Add One To Number

Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints
1 <= size of the array <= 1000000



Input Format
First argument is an array of digits.



Output Format
Return the array of digits after adding one.



Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        result_arr = []
        carry = 1
        end_index = -1
        for i in range(0,len(A)):
            if A[i] != 0:
                end_index = i
                break
        if end_index == -1:
            return [1]
        for i in range(len(A)-1,end_index-1,-1):
            sum_val = A[i] + carry
            digit = sum_val%10
            carry = int(sum_val/10)
            result_arr.append(digit)
        if carry == 1:
            result_arr.append(carry)
    
        result_arr.reverse()
        return result_arr