# This problem is called 1031. Maximum Sum of Two Non-Overlapping Subarrays
# You can access it here: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

# This program will recieve an integer array nums and two other integers firstLen and secondLen. 
# The program will then return the maximum sum of elements in two non-overlapping subarrays 
# with lengths firstLen and secondLen.
# A subarray is a contiguous part of an array.
# For example if nums = [0,6,5,2,2,5,1,9,4] and firstLen = 1 and secondLen = 2
# Then the output will be: 20
# One subarray is: subarray [9] which has the firstLen which is 1 
# The second subarray is: subarray [6,5] which has the secondLen which is 2.

class Solution:
  def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    def helper(l: int, r: int) -> int:
      n = len(nums)
      # Create list left with the same length as nums
      # Create sums to store the total of nums
      left = [0] * n
      sums = 0

      for i in range(n):
        sums += nums[i]
        if i >= l:
          sums -= nums[i - l]
        if i >= l - 1:
          left[i] = max(left[i - 1], sums) if i > 0 else sums

      right = [0] * n
      sums = 0

      for i in reversed(range(n)):
        sums += nums[i]
        if i <= n - r - 1:
          sums -= nums[i + r]
        if i <= n - r:
          right[i] = max(right[i + 1], sums) if i < n - 1 else sums

      return max(left[i] + right[i + 1] for i in range(n - 1))

    return max(helper(firstLen, secondLen), helper(secondLen, firstLen))