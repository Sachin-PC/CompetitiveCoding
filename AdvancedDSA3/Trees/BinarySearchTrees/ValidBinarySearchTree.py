"""
Valid Binary Search Tree

You are given a binary tree represented by root A. You need to check if it is a Binary Search Tree or not.

Assume a BST is defined as follows:

1) The left subtree of a node contains only nodes with keys less than the node's key.

2) The right subtree of a node contains only nodes with keys greater than the node's key.

3) Both the left and right subtrees must also be binary search trees.



Problem Constraints
1 <= Number of nodes in binary tree <= 105

0 <= node values <= 232-1



Input Format
First and only argument is head of the binary tree A.



Output Format
Return 0 if false and 1 if true.



Example Input
Input 1:

 
   1
  /  \
 2    3
Input 2:

 
  2
 / \
1   3


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 2 is not less than 1 but is in left subtree of 1.
Explanation 2:

Satisfies all conditions.
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def isValid(cur_node):

    if cur_node is None:
        return [1, None, None]
    
    cur_node_val = cur_node.val
    [left_is_valid,left_max, left_min] = isValid(cur_node.left)
    [right_is_valid,right_max, right_min] = isValid(cur_node.right)

    if left_is_valid == 0 or right_is_valid == 0:
        # print("cur node = ",cur_node.val," and returning 0")
        return [0, cur_node.val, cur_node.val]
    else:
        max_val = right_max
        min_val = left_min
        if left_max is None:
            left_max = float('-inf')
        if left_min is None:
            min_val = cur_node_val
        if right_max is None:
            max_val = cur_node_val
        if right_min is None:
            right_min = float('inf')
        if cur_node_val > left_max and cur_node_val < right_min:
            # print("cur node = ",cur_node.val," and returning 1")
            # print("[left_is_valid,left_max, left_min] = ",left_is_valid,left_max, left_min)
            # print("[right_is_valid,right_max, right_min] = ",right_is_valid,right_max, right_min)
            # print("returning ",1,max_val, min_val)
            return [1,max_val, min_val]
        else:
            # print("cur node = ",cur_node.val," and returning 0")
            return [0, cur_node.val, cur_node.val]


class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):

        [is_valid_bst, max_val, min_val] = isValid(A)

        return is_valid_bst