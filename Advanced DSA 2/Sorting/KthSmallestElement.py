"""
Q2. Kth Smallest Element

Problem Description
Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

1 <= A[i] <= 109



Input Format
The first argument is an integer array A.

The second argument is integer B.



Output Format
Return the Bth smallest element in given array.



Example Input
Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 2
"""
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
        A = list(A)
        n = len(A)

        small_no = 0
        for i in range(n):
            min_val = float('inf')
            min_val_index = -1
            for k in range(i,n):
                if A[k] < min_val:
                    min_val = A[k]
                    min_val_index = k
            temp = A[i]
            A[i] = min_val
            A[min_val_index] = temp
            small_no += 1
            if small_no == B:
                return min_val
        
                