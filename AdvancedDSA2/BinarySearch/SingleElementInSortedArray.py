"""
Q4. Single Element in Sorted Array

Problem Description
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

Elements which are appearing twice are adjacent to each other.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the single element that appears only once.



Example Input
Input 1:

A = [1, 1, 7]
Input 2:

A = [2, 3, 3]


Example Output
Output 1:

 7
Output 2:

 2


Example Explanation
Explanation 1:

 7 appears once
Explanation 2:

 2 appears once
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        low = 0
        high = n-1
        # mid = (low + high)/2
        while(low <= high):
            mid = int((low+high)/2)
            if mid == 0 or mid == n-1:
                return A[mid]
            if A[mid] != A[mid-1] and A[mid] != A[mid+1]:
                return A[mid]
            elif A[mid] == A[mid-1]:
                if (mid-1)%2 == 0:
                    low = mid+1
                else:
                    high = mid-2
            else:
                if mid%2 == 0:
                    low = mid+2
                else:
                    high = mid-1