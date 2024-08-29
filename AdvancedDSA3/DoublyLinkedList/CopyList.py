"""
Q2. Copy List

Problem Description
You are given a linked list A
Each node in the linked list contains two pointers: a next pointer and a random pointer
The next pointer points to the next node in the list
The random pointer can point to any node in the list, or it can be NULL
Your task is to create a deep copy of the linked list A
The copied list should be a completely separate linked list from the original list, but with the same node values and random pointer connections as the original list
You should create a new linked list B, where each node in B has the same value as the corresponding node in A
The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)


Problem Constraints
0 <= |A| <= 106



Input Format
The first argument of input contains a pointer to the head of linked list A.



Output Format
Return a pointer to the head of the required linked list.



Example Input
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Output
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Explanation
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        
        list_a_map = {}
        list_b_map = {}
        temp = head
        count = 0
        while temp is not None:
            if temp not in list_a_map:
                new_node = RandomListNode(temp.label)
                count += 1
                # list_b_map[new_node] = new_node.label
                list_a_map[temp] = new_node
            temp = temp.next
        # print("count = ",count)
        # print("list_a_map = ",list_a_map)
        temp = head
        new_head = list_a_map[head]
        # new_head.random = list_a_map[temp.random]
        # new_head.next = list_a_map[temp.next]
        # temp = temp.next
        cur_list_node = new_head
        while temp is not None:
            if temp.random is None:
                cur_list_node.random = None
            else:
                cur_list_node.random = list_a_map[temp.random]
            if temp.next is None:
                cur_list_node.next = None
            else:
                cur_list_node.next = list_a_map[temp.next]
            temp = temp.next
            cur_list_node = cur_list_node.next

        return new_head

