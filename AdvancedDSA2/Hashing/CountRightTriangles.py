"""
Q1. Count Right Triangles

Problem Description
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

NOTE: The answer may be large so return the answer modulo (109 + 7).



Problem Constraints
1 <= N <= 105

0 <= A[i], B[i] <= 109



Input Format
The first argument given is an integer array A.
The second argument given is the integer array B.



Output Format
Return the number of unordered triplets that form a right angled triangle modulo (109 + 7).



Example Input
Input 1:

 A = [1, 1, 2]
 B = [1, 2, 1]
Input 2:

 A = [1, 1, 2, 3, 3]
 B = [1, 2, 1, 2, 1]


Example Output
Output 1:

 1
Output 2:

 6


Example Explanation
Explanation 1:

 All three points make a right angled triangle. So return 1.
Explanation 2:

 6 triplets which make a right angled triangle are:    (1, 1), (1, 2), (2, 1)
                                                       (1, 1), (3, 1), (1, 2)
                                                       (1, 1), (3, 1), (3, 2)
                                                       (2, 1), (3, 1), (3, 2)
                                                       (1, 1), (1, 2), (3, 2)
                                                       (1, 2), (3, 1), (3, 2)
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        map_x = {}
        map_y = {}
        n = len(A)
        mod_val = 10**9 + 7
        for i in range(n):
            x = A[i]
            y = B[i]
            if x in map_x:
                map_x[x] += 1
            else:
                map_x[x] = 1

            if y in map_y:
                map_y[y] += 1
            else:
                map_y[y] = 1

        # print("map_x = ",map_x)
        # print("map_y = ",map_y)
        
        total_right_triangles = 0
        for i in range(n):
            x = A[i]
            y = B[i]
            no_of_same_y_x = map_y[y] - 1
            no_of_same_x_y = map_x[x] - 1
            total_right_triangles = (total_right_triangles + (no_of_same_y_x*no_of_same_x_y)%mod_val )%mod_val

        return total_right_triangles