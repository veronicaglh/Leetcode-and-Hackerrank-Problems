# This problem is called 1679. Max Number of K-Sum Pairs
# You can access it here: https://leetcode.com/problems/max-number-of-k-sum-pairs/

# This program will recieve a list of integers(named nums) and another integer, k.
# In one operation, it is allowed to pick two numbers from the array whose sum equals k and remove them from the array.
# The program will return the maximum number of operations you can perform on the array.
# For example if nums = [1,2,3,4] and k = 5
# Then output = 2
# Beacause:
# Starting with nums = [1,2,3,4]:
# - The program will remove numbers 1 and 4, then nums = [2,3]
# - then remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        pairs = 0

        for num in nums:
            complement = k - num
            if complement in counts:
                if counts[num] > 0 and counts[complement] > 0:
                    if num == complement and counts[num] < 2: 
                        continue
                    pairs += 1
                    counts[num] -= 1
                    counts[complement] -= 1
        return pairs
