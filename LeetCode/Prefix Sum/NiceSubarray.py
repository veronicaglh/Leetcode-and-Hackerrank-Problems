# This problem is called 1248. Count Number of Nice Subarrays
# You can access it here: https://leetcode.com/problems/count-number-of-nice-subarrays/


# The program recieves an array of integers called nums and an integer k.
# A continuous subarray is called nice if there are k odd numbers on it. 
# The program will return the number of nice subarrays there are in nums.
# For example if nums =  [1,1,2,1,1] and k = 3. 
# The output will be 2 
# Because there are only 2 subarrays with 3 odd numbers. 
# The subarrays are [1,1,2,1] and [1,2,1,1].
# If nums = [2,4,6] and k = 1
# The output will be  0 
# Because there is no subarray which contains an odd number.

class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def numberOfSubarraysAtMost(k: int) -> int:
      counter = 0
      l = 0
      r = 0

      while r <= len(nums):
        if k >= 0:
          counter += r - l
          if r == len(nums):
            break
          if nums[r] & 1==1:
            k -= 1
          r += 1
        else:
          if nums[l] & 1==1:
            k += 1
          l += 1
      return counter

    return numberOfSubarraysAtMost(k) - numberOfSubarraysAtMost(k - 1)