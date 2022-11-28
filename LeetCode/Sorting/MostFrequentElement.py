# This problem is called 1838. Frequency of the Most Frequent Element
# You can access it here: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

# This program will recieve a list of integers(named nums) and another integer value, k.
# In one operation, it is possible to choose an index of nums and increment the element at that index by 1.
# The program will return the maximum possible frequency of an element after performing at most k operations.
# For example if nums = [1,2,4] and k = 5
# Then output = 3
# Beacause increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        window = 0
        l, r, n = 0, 1, len(nums)
        while r < n:
            window += (nums[r] - nums[r - 1]) * (r - l)
            r += 1
            while window > k:
                window -= nums[r - 1] - nums[l]
                l += 1
            result = max(result, r - l)
        return result
