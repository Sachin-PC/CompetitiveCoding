"""
Q4. Delete in Linked List

Problem Description
You are given the head of a linked list A and an integer B. Delete the B-th node from the linked list.

Note : Follow 0-based indexing for the node numbering.



Problem Constraints
1 <= size of linked list <= 105
1 <= value of nodes <= 109
0 <= B < size of linked list



Input Format
The first argument A is the head of a linked list.

The second arguement B is an integer.



Output Format
Return the head of the linked list after deletion



Example Input
Input 1:
A = 1 -> 2 -> 3
B = 1
Input 2:
A = 4 -> 3 -> 2 -> 1
B = 0


Example Output
Output 1:
1 -> 3
Output 2:
3 -> 2 -> 1


Example Explanation
For Input 1:
The linked list after deletion is 1 -> 3.
For Input 2:
The linked list after deletion is 3 -> 2 -> 1.
"""
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        temp = A
        pos = 0
        prev = None
        while temp is not None:
            if pos == B:
                if prev is None:
                    return temp.next
                else:
                    prev.next = temp.next
                    return A
            else:
                prev = temp
                temp = temp.next
            pos += 1

        return []