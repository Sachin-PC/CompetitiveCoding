"""
Q3. Merge Intervals - 2

Problem Description
You have a set of non-overlapping intervals. You are given a new interval [start, end], insert this new interval into the set of intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints
0 <= |intervals| <= 105



Input Format
First argument is the vector of intervals

second argument is the new interval to be merged



Output Format
Return the vector of intervals after merging



Example Input
Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output
Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]


Example Explanation
Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals
"""
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def insert(self, A, B):
        n = len(A)
        merged_intervals = []
        if n == 0:
            merged_intervals.append(B)
            return merged_intervals
        if B[0] < A[0][0]:
            start = B[0]
            end = B[1]
            i = 0
            flag = 1
        else:
            start = A[0][0]
            end = A[0][1]
            i =0
            flag = 0

        while i < n:
            # print("i= ",i)
            if flag == 0 and (B[0] < A[i][0]) :
                new_start = B[0]
                new_end = B[1]
                flag = 1
                i -= 1
            else:
                new_start = A[i][0]
                new_end = A[i][1]
            if end < new_start:
                merged_intervals.append([start,end])
                start = new_start
                end = new_end
            else:
                end = max(end,new_end)
            
            i += 1

        if flag == 0 and (B[0] >= A[i-1][0]):
            new_start = B[0]
            new_end = B[1]
            if end < new_start:
                merged_intervals.append([start,end])
                start = new_start
                end = new_end
            else:
                end = max(end,new_end)
        merged_intervals.append([start,end])

        return merged_intervals