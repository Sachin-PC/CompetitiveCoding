"""
Q4. Level Order

Problem Description
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return a 2D integer array denoting the level order traversal of the given binary tree.



Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.
"""
from queue import Queue

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        level_queue = Queue()
        level_queue.put(A)
        level_queue.put(None)
        # print("level_queue = ",level_queue)
        res = []
        row_list = []
        flag = 0
        while level_queue:
            cur_node = level_queue.get()
            if cur_node is None:
                if flag == 1:
                    break
                # print("cur node is None")
                res.append(row_list)
                level_queue.put(None)
                row_list = []
                flag = 1
            else:
                flag = 0
                # print("cur node = ",cur_node.val)
                row_list.append(cur_node.val)
                if cur_node.left is not None:
                    level_queue.put(cur_node.left)
                if cur_node.right is not None:
                    level_queue.put(cur_node.right)
        # res.append(row_list)

        return res
                    