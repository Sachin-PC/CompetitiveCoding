"""
Q2. Vertical Order traversal

Problem Description
Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.


NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.



Problem Constraints
0 <= number of nodes <= 105



Input Format
First and only arument is a pointer to the root node of binary tree, A.



Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.



Example Input
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

      1
    /   \
   3     7
  /       \
 2         9


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]


Example Explanation
Explanation 1:

 First row represent the verical line 1 and so on.
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from queue import Queue

def levelOT(A,res,vertical_distance_map,min_dist):

    # print("res size = ",len(res))
    level_queue = Queue()
    level_queue.put(A)
    level_queue.put(None)
    # print("level_queue = ",level_queue)
    row_list = []
    flag = 0
    cur_level = 0
    while level_queue:
        cur_node = level_queue.get()
        if cur_node is None:
            if flag == 1:
                break
            cur_level += 1
            level_queue.put(None)
            flag = 1
        else:
            flag = 0
            # print("cur node = ",cur_node.val)
            node_dist_tuples = vertical_distance_map[cur_node.val]
            # dist_index = node_dist.pop(0) + abs(min_dist)
            # res[dist_index].append(cur_node.val)
            for i in range(len(node_dist_tuples)):
                if node_dist_tuples[i][1] == cur_level:
                    dist_index = node_dist_tuples[i][0]+abs(min_dist)
                    res[dist_index].append(cur_node.val)
                    node_dist_tuples[i][1] = -1
                    break
            if cur_node.left is not None:
                level_queue.put(cur_node.left)
            if cur_node.right is not None:
                level_queue.put(cur_node.right)
    return

def levelOrderTraversal(A,res,vertical_distance_map,min_dist):
    level_order_queue = Queue()
    level_order_queue.put(A)
    level_order_queue.put(None)
    flag = 0
    while level_order_queue is not None:
        cur_node = level_order_queue.get()
        if cur_node is None:
            if flag == 1:
                break
            flag = 1
        else:
            flag = 0
            node_dist = vertical_distance_map[cur_node.val]
            for i in range(len(node_dist)):
                dist_index = node_dist[i]+abs(min_dist)
                res[dist_index].append(cur_node.val)
            
            if cur_node.left is not None:
                level_order_queue.put(cur_node.left)
            if cur_node.right is not None:
                level_order_queue.put(cur_node.right)
    return
        

def verticalTraversal(cur_node,distance,vertical_distance_map,level):
    if cur_node is None:
        return [None,None]
    else:
        if cur_node.val in vertical_distance_map:
            vertical_distance_map[cur_node.val].append([distance,level])
        else:
            vertical_distance_map[cur_node.val] = [[distance,level]]
        [left_max_dist, left_min_dist] = verticalTraversal(cur_node.left,distance-1,vertical_distance_map,level+1)
        if left_max_dist is None:
            left_max_dist = distance
        if left_min_dist is None:
            left_min_dist = distance
        [right_max_dist, right_min_dist] = verticalTraversal(cur_node.right,distance+1,vertical_distance_map,level+1)
        if right_max_dist is None:
            right_max_dist = distance
        if right_min_dist is None:
            right_min_dist = distance
        max_dist = max(left_max_dist, right_max_dist)
        min_dist = min(left_min_dist, right_min_dist)
        return [max_dist,min_dist]



class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
        vertical_distance_map = {}
        [max_dist,min_dist] = verticalTraversal(A,0,vertical_distance_map,0)


        res = []
        # print(f"max = {max_dist}, min = {min_dist}")
        for i in range(min_dist,max_dist+1):
            res.append([])

        # print("vertical_distance_map[-4] = ",vertical_distance_map[-4])
        # levelOrderTraversal(A,res,vertical_distance_map,min_dist)

        # print("vertical_distance_map = ",vertical_distance_map)
        # print("vertical_distance_map[454] = ",vertical_distance_map[454])
        matching_keys = []
        for key, value in vertical_distance_map.items():
            for i in range(len(value)):
                if value[i] == -4:
                    matching_keys.append(key)
        # print("matching keys = ",matching_keys)
        levelOT(A,res,vertical_distance_map,min_dist)
        # print("res = ",res)
        return res
