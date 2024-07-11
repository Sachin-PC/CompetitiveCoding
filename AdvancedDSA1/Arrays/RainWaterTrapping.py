"""
Q3. Rain Water Trapped

Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
First and only argument is the vector A



Output Format
Return one integer, the answer to the question



Example Input
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

1 unit is trapped on top of the 3rd element.
Explanation 2:

No water is trapped.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left_block = [0]*n
        max_right_block = [0]*n
        max_block_size_left = 0
        max_block_size_right = 0
        for i in range(n):
            #left_block
            max_block_size_left = max(max_block_size_left, height[i])
            max_left_block[i] = max_block_size_left

            #right_block
            max_block_size_right = max(max_block_size_right, height[n-i-1])
            max_right_block[n-i-1] = max_block_size_right

        total_water_trapped = 0
        for i in range(n):
            total_water_trapped += (min(max_left_block[i],max_right_block[i]) - height[i])

        return total_water_trapped