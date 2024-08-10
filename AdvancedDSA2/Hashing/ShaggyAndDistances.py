"""
Q2. Shaggy and distances
Problem Description
Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.

Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.



Problem Constraints
1 <= |A| <= 105



Input Format
The first and only argument is an integer array A.



Output Format
Return one integer corresponding to the minimum possible distance between a special pair.



Example Input
Input 1:

A = [7, 1, 3, 4, 1, 7]
Input 2:

A = [1, 1]


Example Output
Output 1:

 3
Output 2:

 1

"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        num_dict = {}

        min_dist = len(A)
        for i in range(len(A)):
            num = A[i]
            if num in num_dict:
                start_index = num_dict[num]
                if (i - start_index) < min_dist:
                    min_dist = i - start_index
            num_dict[num] = i
        
        if min_dist == len(A):
            return -1
        else:
            return min_dist
