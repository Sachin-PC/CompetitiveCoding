"""
Q4. Delete a node in BST

Problem Description
Given a Binary Search Tree(BST) A. If there is a node with value B present in the tree delete it and return the tree.

Note - If there are multiple options, always replace a node by its in-order predecessor


Problem Constraints
2 <= No. of nodes in BST <= 105
1 <= value of nodes <= 109
Each node has a unique value


Input Format
The first argument is the root node of a Binary Search Tree A.
The second argument is the value B.


Output Format
Delete the given node if found and return the root of the BST.


Example Input
Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 10

Input 2:

            8
           / \
          6  21
         / \
        1   7

     B = 6



Example Output
Output 1:

            15
          /    \
        12      20
        / \    /  \
       8  14  16  27

Output 2:

            8
           / \
          1  21
           \
            7



Example Explanation
Explanation 1:

Node with value 10 is deleted 
Explanation 2:

Node with value 6 is deleted 
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def delNode(parent_node,cur_node,B):
    if cur_node.val == B:
        if cur_node.left is None and cur_node.right is None:
            linking_node = None
        elif cur_node.left is None:
            linking_node = cur_node.right
        elif cur_node.right is None:
            linking_node = cur_node.left
        else:
            left_max_node = cur_node.left
            if left_max_node.right is None:
                linking_node = left_max_node
                linking_node.right = cur_node.right
            else:
                prev_node = cur_node
                while left_max_node.right is not None:
                    prev_node = left_max_node
                    left_max_node = left_max_node.right
                prev_node.right = left_max_node.left
                linking_node = left_max_node
                linking_node.left = cur_node.left
                linking_node.right = cur_node.right

        # print("cur_node = ",cur_node.val)
        # if parent_node is None:
        #     print("parent_node = ",None)
        # else:
        #     print("parent_node = ",parent_node.val)
        # if linking_node is None:
        #     print("linking_node = None")
        # else:
        #     print("linking_node = ",linking_node.val)
        if parent_node is None:
            if linking_node is None:
                return -1
            else:
                return linking_node
        else:
            if parent_node.left == cur_node:
                # print("linkinf parent left")
                parent_node.left = linking_node
            else:
                # print("linkinf parent right")
                parent_node.right = linking_node
        return None

    elif B < cur_node.val:
        ret_head = delNode(cur_node,cur_node.left,B)
        return ret_head
    else:
        ret_head = delNode(cur_node,cur_node.right,B)
        return ret_head

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def solve(self, A, B):

        parent = None
        head_node = delNode(parent,A,B)
        if head_node is None:
            return A
        elif head_node == -1:
            return None
        else:
            return head_node