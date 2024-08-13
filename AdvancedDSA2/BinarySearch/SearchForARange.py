"""
Q3. Search for a Range

Problem Description
Given a sorted array of integers A (0-indexed) of size N, find the left most and the right most index of a given integer B in the array A.

Return an array of size 2, such that 
          First element = Left most index of B in A
          Second element = Right most index of B in A.
If B is not found in A, return [-1, -1].

Note : Your algorithm's runtime complexity must be in the order of O(log n).


Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the left most and right most index (0-based) of B in A as a 2-element array. If B is not found in A, return [-1, -1].


Example Input
Input 1:

 A = [5, 7, 7, 8, 8, 10]
 B = 8
Input 2:

 A = [5, 17, 100, 111]
 B = 3


Example Output
Output 1:

 [3, 4]
Output 2:

 [-1, -1]
"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        n = len(A)

        #finding left most index
        low = 0
        high = n-1
        left_index = -1
        while low <= high:
            mid = int((low+high)/2)
            if A[mid] == B:
                if mid == 0:
                    left_index = mid
                    break
                elif A[mid-1] != B:
                    left_index = mid
                    break
                else:
                    high = mid-1
            elif A[mid] < B:
                low = mid+1
            else:
                high = mid-1
        if left_index == -1:
            return [-1,-1]

        low = 0
        high = n-1
        right_index = -1
        while low <= high:
            mid = int((low+high)/2)
            if A[mid] == B:
                if mid == n-1:
                    right_index = mid
                    break
                elif A[mid+1] != B:
                    right_index = mid
                    break
                else:
                    low = mid+1
            elif A[mid] < B:
                low = mid+1
            else:
                high = mid-1

        return [left_index, right_index]