"""
Q1. Balanced Paranthesis

Problem Description
Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.



Problem Constraints
1 <= |A| <= 100



Input Format
The first and the only argument of input contains the string A having the parenthesis sequence.



Output Format
Return 0 if the parenthesis sequence is not balanced.

Return 1 if the parenthesis sequence is balanced.



Example Input
Input 1:

 A = {([])}
Input 2:

 A = (){
Input 3:

 A = ()[] 


Example Output
Output 1:

 1 
Output 2:

 0 
Output 3:

 1 


Example Explanation
You can clearly see that the first and third case contain valid paranthesis.

In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.
"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        paranthesis_stack = []
        open_paranthesis = {'{','(','['}
        closed_paranthesis = {'}',')',']'}
        paranthesis_mapping = {}
        paranthesis_mapping['}'] = '{'
        paranthesis_mapping[')'] = '('
        paranthesis_mapping[']'] = '['
        for char in A:
            if char in open_paranthesis:
                paranthesis_stack.append(char)
            elif char in closed_paranthesis:
                if paranthesis_stack:
                    if paranthesis_stack[-1] == paranthesis_mapping[char]:
                        paranthesis_stack.pop()
                else:
                    return 0
            else:
                return 0
        if not paranthesis_stack:
            return 1
        else:
            return 0