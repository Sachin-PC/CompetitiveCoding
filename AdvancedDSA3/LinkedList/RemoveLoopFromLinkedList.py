"""
Q1. Remove Loop from Linked List

Problem Description
You are using Google Maps to help you find your way around a new place. But, you get lost and end up walking in a circle. Google Maps has a way to keep track of where you've been with the help of special sensors.These sensors notice that you're walking in a loop, and now, Google wants to create a new feature to help you figure out exactly where you started going in circles.

Here's how we can describe the challenge in simpler terms: You have a Linked List A that shows each step of your journey, like a chain of events. Some of these steps have accidentally led you back to a place you've already been, making you walk in a loop. The goal is to find out the exact point where you first started walking in this loop, and then you want to break the loop by not going in the circle just before this point.




Problem Constraints
1 <= number of nodes <= 1000



Input Format
The first of the input contains a LinkedList, where the first number is the number of nodes N, and the next N nodes are the node value of the linked list.
The second line of the input contains an integer which denotes the position of node where cycle starts.



Output Format
return the head of the updated linked list.



Example Input
Input 1:

 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output
Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL


Example Explanation
Explanation 1:

 Chain of 1->2 is broken.
Explanation 2:

 Chain of 4->6 is broken.
"""
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if A is None:
            return A

        # temp = A
        # count = 0
        # while temp is not None:
        #     print(temp.val)
        #     temp = temp.next
        #     if count == 40:
        #         break
        #     count += 1

        slow_pointer = A
        fast_pointer = A.next
        # print("NOO")
        while fast_pointer is not None:
            # print("fast_pointer.val = ",fast_pointer.val)
            if slow_pointer == fast_pointer:
                # print("mid val = ",slow_pointer.val)
                P2 = slow_pointer.next
                break
            else:
                prev_p2 = slow_pointer
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
                if fast_pointer is not None:
                    fast_pointer = fast_pointer.next

        # print("YESSS")
        if fast_pointer is not None:
            P1 = A
            while P1 != P2:
                # print("P1 = ",P1.val," P2 = ",P2.val)
                P1 = P1.next
                prev_p2 = P2
                P2 = P2.next

            prev_p2.next = None

        # print("prev_p2 = ",prev_p2.val)
        # count = 1
        # temp = A
        # while temp is not None:
        #     if count == 5:
        #         temp.next = None
        #         return A
        #     temp = temp.next
        #     count += 1

        return A

        