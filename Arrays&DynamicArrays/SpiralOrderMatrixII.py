"""
Q1. Spiral Order Matrix II
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.



Problem Constraints
1 <= A <= 1000



Input Format
First and only argument is integer A


Output Format
Return a 2-D matrix which consists of the elements added in spiral order.



Example Input
Input 1:

1
Input 2:

2
Input 3:

5


Example Output
Output 1:

[ [1] ]
Output 2:

[ [1, 2], 
  [4, 3] ]
Output 3:

[ [1,   2,  3,  4, 5], 
  [16, 17, 18, 19, 6], 
  [15, 24, 25, 20, 7], 
  [14, 23, 22, 21, 8], 
  [13, 12, 11, 10, 9] ]

"""

import numpy as np

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        sprial_matrix = np.zeros((A,A))
        i = 1
        end_val = A*A
        max_row = A-1
        max_col = A-1
        min_row = 0
        min_col = 0
        flag = 0
        cur_row = 0
        cur_col=0
        while i <= end_val:
            sprial_matrix[cur_row,cur_col] = i
            i += 1
            if flag == 0:
                cur_col += 1
                if cur_col > max_col:
                    cur_col = max_col
                    cur_row = min_row + 1
                    flag = 1
            elif flag == 1:
                cur_row += 1
                if cur_row > max_col:
                    cur_row = max_row
                    cur_col = max_col-1
                    flag = 2
            elif flag == 2:
                cur_col -= 1
                if cur_col < min_col:
                    cur_col = min_col
                    cur_row = max_row - 1
                    flag = 3
            elif flag == 3:
                cur_row -= 1
                if cur_row == min_row:
                    min_row += 1
                    min_col += 1
                    max_row -= 1
                    max_col -= 1
                    cur_row = min_row
                    cur_col = min_col
                    flag = 0
        
        return np.array(sprial_matrix).astype(int)