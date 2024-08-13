"""
Q2. Rotated Sorted Array Search

Problem Description
Given a sorted array of integers A of size N and an integer B, 
where array A is rotated at some pivot unknown beforehand.

For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.

You can assume that no duplicates exist in the array.

NOTE: You are expected to solve this problem with a time complexity of O(log(N)).


Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 109
All elements in A are Distinct.


Input Format
The First argument given is the integer array A.
The Second argument given is the integer B.


Output Format
Return index of B in array A, otherwise return -1


Example Input
Input 1:

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4 
Input 2:

A : [ 9, 10, 3, 5, 6, 8 ]
B : 5


Example Output
Output 1:

 0 
Output 2:

 3


Example Explanation
Explanation 1:

Target 4 is found at index 0 in A. 
Explanation 2:

Target 5 is found at index 3 in A.
"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)
        if n == 1: 
            if A[0] == B:
                return 0
            else:
                return -1

        is_rotated = False
        if A[0] > A[n-1]:
            is_rotated = True
        
        low = 0
        high = n-1

        if is_rotated:
            low = 0
            high = n-1
            while low <= high:
                mid = int((low+high)/2)
                if A[mid] > A[mid+1]:
                    e1 = mid
                    s2 = mid+1
                    break
                else:
                    if A[mid] > A[n-1]:
                        low = mid+1
                    else:
                        high = mid-1 

            s1 = 0
            if B < A[0]:
                low = s2
                high = n-1
            else:
                low = 0
                high = e1
        
        # print("low = ",low," high = ",high)
        while low <= high:
            mid = int((low+high)/2)
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                high = mid-1
            else:
                low = mid+1

        return -1
            
