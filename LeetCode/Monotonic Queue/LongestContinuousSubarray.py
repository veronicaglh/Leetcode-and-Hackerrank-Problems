# This problem is called 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# You can access it here: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

# The program recieves an array of integers named nums and an integer value limit.
# It will return the size of the longest non-empty subarray such that the
# absolute difference between any two elements of this subarray is less than or equal to limit.
# For example: if  nums = [8,2,4,7] and limit = 4
# Then the output will be 2 

import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq, min_dq = collections.deque(), collections.deque()
        left = 0
        for right, num in enumerate(nums):
            while max_dq and nums[max_dq[-1]] <= num:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and nums[min_dq[-1]] >= num:
                min_dq.pop()
            min_dq.append(right)
            if nums[max_dq[0]]-nums[min_dq[0]] > limit:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1  # advance left by one to not count in result
        return len(nums)-left
