"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        n = len(sorted_intervals)
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        merged_intervals = []
        flag = 0
        for i in range(1,n):
            new_start = sorted_intervals[i][0]
            new_end = sorted_intervals[i][1]
            if end < new_start:
                merged_intervals.append([start,end])
                start = new_start
                end = new_end
            else:
                end = max(end,new_end)
        
        merged_intervals.append([start,end])

        return merged_intervals