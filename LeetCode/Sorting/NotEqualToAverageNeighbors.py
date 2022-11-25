# This problem is called 1968. Array With Elements Not Equal to Average of Neighbors
# You can access it here: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

# This program will recieve a list of distinct integers 
# It will rearrange the elements in the array such that 
# every element in the rearranged array is not equal to the average of its neighbors.
# For example if nums = [1,2,3,4,5]
# Then output =  [1,2,4,5,3]
# Because: 
# When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
# When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
# When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        final_result = []

        left = 0
        right = len(nums) - 1 
        
        while len(final_result) != len(nums):
            final_result.append(nums[left])
            left += 1

            if left <= right:
                final_result.append(nums[right])
                right -= 1 
        return final_result