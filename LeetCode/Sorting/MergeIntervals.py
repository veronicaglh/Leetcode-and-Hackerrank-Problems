# This problem is called 56. Merge Intervals
# You can access it here: https://leetcode.com/problems/merge-intervals/

# This program will recieve a list of integers intervals where intervals[i] = [starti, endi]
# The program will erge all overlapping intervals, and return an array of the non-overlapping 
# intervals that cover all the intervals in the input.
# For example if intervals = [[1,3],[2,6],[8,10],[15,18]]
# Then output =  [[1,6],[8,10],[15,18]]
# Since intervals [1,3] and [2,6] overlap, the program will merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        merged_intervals = []
        for i in intervals:
            newInterval = i
            if  len(merged_intervals) != 0:
                if  merged_intervals[-1][1] >= i[0]: 
                    newInterval =  merged_intervals.pop()
                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]      
            merged_intervals.append(newInterval)
        return  merged_intervals
