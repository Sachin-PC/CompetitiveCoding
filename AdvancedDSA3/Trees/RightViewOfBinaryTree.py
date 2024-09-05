"""
Q1. Right View of Binary tree

Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an array, representing the right view of the binary tree.



Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]


Example Explanation
Explanation 1:

Right view is described.
Explanation 2:

Right view is described.
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from queue import Queue

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        level_queue = Queue()
        level_queue.put(A)
        level_queue.put(None)
        flag = 0
        res = []
        while level_queue:
            cur_node = level_queue.get()
            if cur_node is None:
                if flag == 1:
                    break
                else:
                    res.append(prev_val)
                    level_queue.put(None)
                    flag = 1
            else:
                flag = 0
                if cur_node.left is not None:
                    level_queue.put(cur_node.left)
                if cur_node.right is not None:
                    level_queue.put(cur_node.right)
                prev_val = cur_node.val

        return res