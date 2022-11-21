# This problem is called 75. Sort Colors
# You can access it here: https://leetcode.com/problems/sort-colors/

# This program will recieve a list of integers(named nums) with n objects colored red, white, or blue.
# The program will sort them in place so that objects of the same color are adjacent 
# with the colors in the order red, white, and blue.
# Numbers 0, 1 and 2 will represent the color red, white, and blue, respectively.
# The program can not use the libraries sort function.
# For example if nums = [2,0,2,1,1,0]
# Then the output will be [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
   
        final_nums = []

        for i in range(len(nums)):
            final_nums.append(min(nums))
            nums.remove(min(nums))

        for i in final_nums:
            nums.append(i)

        print(nums)