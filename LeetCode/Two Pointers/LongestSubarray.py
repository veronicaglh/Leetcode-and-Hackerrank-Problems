# This problem is called 1493. Longest Subarray of 1's After Deleting One Element
# You can access it here: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

# The program will be given a binary array nums, and it will delete one element from it.
# The program will return the size of the longest non-empty subarray containing only 1's 
# in the resulting array. Return 0 if there is no such subarray.
# For example if nums = [1,1,0,1]
# Then the output will be 3.
# Because after deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        K = 1
        n = len(nums)
        result = 0

        for j in range(n):
            if nums[j] == 0:
                K-=1

            while count < n and K < 0:
                if nums[count] == 0:
                    K+=1
                count+=1

            result = max(result,j-count+1)

        return result - 1
 