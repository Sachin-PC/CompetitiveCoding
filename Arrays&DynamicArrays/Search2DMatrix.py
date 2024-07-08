"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        total_nums = n*m
        low = 0
        high = total_nums - 1
        cur_row = 0
        while low <= high:
            mid = int((low + high)/2)
            row = int(mid/m)
            col = int(mid%m)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            elif matrix[row][col] > target:
                high = mid - 1

        return False