"""
Q2. Binary Tree From Inorder And Postorder

Problem Description
Given the inorder and postorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.



Problem Constraints
1 <= number of nodes <= 105



Input Format
First argument is an integer array A denoting the inorder traversal of the tree.

Second argument is an integer array B denoting the postorder traversal of the tree.



Output Format
Return the root node of the binary tree.



Example Input
Input 1:

 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:

 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]


Example Output
Output 1:

   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3


Example Explanation
Explanation 1:

 Create the binary tree and return the root node of the tree.
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def build_tree(inorder_data, postorder_data):
    # print("inorder data = ",inorder_data)
    # print("postorde data = ",postorder_data)
    if inorder_data:
        cur_node_val = postorder_data[-1]
        cur_node = TreeNode(cur_node_val)
        val_index = inorder_data.index(cur_node_val)
        n = len(inorder_data)
        left_nodes_inorder_data = inorder_data[0:val_index]
        if val_index == n-1:
            right_nodes_inorder_data = []
        else:
            right_nodes_inorder_data = inorder_data[val_index+1:n]
        left_nodes_post_order = postorder_data[0:val_index]
        if val_index == n-1:
            right_nodes_post_order = []
        else:
            right_nodes_post_order = postorder_data[val_index:n-1] #because we are not including the root node value
        # print(f"Getting left tree for node {cur_node_val}")
        left_node = build_tree(left_nodes_inorder_data, left_nodes_post_order)
        if left_node is not None:
            cur_node.left = left_node
        # print(f"Getting right tree for node {cur_node_val}")
        right_node = build_tree(right_nodes_inorder_data, right_nodes_post_order)
        if right_node is not None:
            cur_node.right = right_node
        return cur_node
    else:
        return None
        

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        root_node = build_tree(A, B)
        return root_node