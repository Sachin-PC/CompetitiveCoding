"""
Q3. Balanced Binary Tree

Problem Description
Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the root of the tree A.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input
Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def check_balance(cur_node):
    if cur_node is None:
        return 0
    else:
        if cur_node.left is None:
            left_tree_height = 0
        else:
            x = check_balance(cur_node.left)
            if x == -1:
                return -1
            else:
                left_tree_height = 1 + x
        if cur_node.right is None:
            right_tree_height = 0
        else:
            y = check_balance(cur_node.right)
            if y == -1:
                return -1
            else:
                right_tree_height = 1 + y
        if abs(right_tree_height - left_tree_height) <= 1:
            return max(left_tree_height, right_tree_height)
        else:
            return -1

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
        is_balanced = check_balance(A)
        if is_balanced == -1:
            return 0
        else:
            return 1