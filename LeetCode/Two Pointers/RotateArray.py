# This problem is called 189. Rotate Array
# You can access it here: https://leetcode.com/problems/rotate-array/

# The program recieves an integer array named nums and a non-negative integer k.
# The program will then rotate the array to the right by k steps
# It will return the rotated array 
# For example if nums = [1,2,3,4,5,6,7] and k = 3 
# Then the output will be [5,6,7,1,2,3,4]
# When the array rotates one step to the right: [7,1,2,3,4,5,6]
# Rotating the array two steps to the right: [6,7,1,2,3,4,5]
# Rotating the array three steps to the right: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
            """
        nums[:] = nums[len(nums) - k: len(nums)] + nums[0:len(nums) - k]