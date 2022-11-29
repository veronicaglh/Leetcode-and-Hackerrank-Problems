# This problem is called 862. Shortest Subarray with Sum at Least K
# You can access it here: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# A subarray is a contiguous part of an array.
# The program recieves an integer array nums and an integer k.
# The program will return the length of the shortest non-empty subarray 
# of nums with a sum of at least k. 
# If there is no such subarray the program will return -1.
# For example if nums = [1] and k = 1
# The output will be 1
# For example nums = [1,2] and k = 4
# The output will be -1

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0]

        for i in range(n):
            pre_sum.append(nums[i] + pre_sum[-1])

        queue = collections.deque()
        result = sys.maxsize 

        for right, s in enumerate(pre_sum):
            while queue and s - pre_sum[queue[0]] >= k:
                result = min(result, right - queue.popleft())

            while queue and s <= pre_sum[queue[-1]]:
                queue.pop()

            queue.append(right)

        if result<sys.maxsize:
            return result
        else: 
            return -1
