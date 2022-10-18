# This problem is called 724. Find Pivot Index.
# You can access it here: https://leetcode.com/problems/find-pivot-index/


# The program recieves an array of numbers called nums
# and will return the pivot index. 
# The pivot index is the index where the sum of all the numbers strictly to the left 
# of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array,
# then the left sum is 0 because there are no elements to the left. 
# This also applies to the right edge of the array.
# The program will return the leftmost pivot index. If no such index exists, th program returns -1.
# For example if nums = [1,7,3,6,5,6]
# The program returns 3 
# Because the pivot index is 3 
# Meaning that: 
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0 
        total = 0 

        # Add each value in nums to total. 
        # Total will be the sum of the values in nums.
        for i in range(len(nums)): 
            total += nums[i]
        
        for i in range(len(nums)): 
            if left_sum == total - nums[i] - left_sum:
                return i
            left_sum += nums[i]
            
        return -1