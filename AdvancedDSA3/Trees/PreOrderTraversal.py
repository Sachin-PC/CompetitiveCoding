"""
Q3. Preorder Traversal

Problem Description
Given a binary tree, return the preorder traversal of its nodes values.



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return an integer array denoting the preorder traversal of the given binary tree.



Example Input
Input 1:

   1
    \
     2
    /
   3
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [1, 2, 3]
Output 2:

 [1, 6, 2, 3]


Example Explanation
Explanation 1:

 The Preoder Traversal of the given tree is [1, 2, 3].
Explanation 2:

 The Preoder Traversal of the given tree is [1, 6, 2, 3].
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def get_pre_order(node, preorder_data):
    if node is None:
        return
    else:
        preorder_data.append(node.val)
        get_pre_order(node.left, preorder_data)
        get_pre_order(node.right, preorder_data)

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        preorder_data = []
        get_pre_order(A, preorder_data)
        return preorder_data