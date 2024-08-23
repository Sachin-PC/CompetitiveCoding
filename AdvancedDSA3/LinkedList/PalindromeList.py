"""
Q2. Palindrome List

Problem Description
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.



Problem Constraints
1 <= |A| <= 105



Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format
Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input
Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output
Output 1:

 1 
Output 2:

 0 


Example Explanation
Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
        n = 0
        temp = A
        while temp is not None:
            n += 1
            temp = temp.next

        if n == 1:
            return 1
        
        mid = int(n/2)
        if n%2 == 1:
            mid += 1

        # print("mid = ",mid)

        count = 1
        temp = A
        mid_node = None
        while count <= mid:
            mid_node = temp 
            temp = temp.next
            count += 1

        # print("temp.val = ",temp.val)
        # print("mid_node.val = ",temp.val)
        if temp.next is not None:
            cur = temp.next
            temp.next = None
            prev = temp
            next_node = None
            while cur.next is not None:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            cur.next = prev
            mid_node.next = cur

            temp = A
        
        p1 = A
        p2 = mid_node.next
        while p1 is not None and p2 is not None and p1 is not mid_node.next:
            if p1.val != p2.val:
                return 0
            p1 = p1.next
            p2 = p2.next
        
        return 1
        
        