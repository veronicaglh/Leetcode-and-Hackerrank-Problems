# This problem is called 283. Move Zeroes
# You can access it here: https://leetcode.com/problems/move-zeroes/

# The program recieves an integer array nums which contains zero values as well as non-zero values.
# It will then return the list with all the zero values moved to the end of the list 
# and all non-zero values at the beginning of the list
# While the order of the non-zero values remains unchanged. 
# For example if nums = [0,1,0,3,12]
# Then the output will be: [1,3,12,0,0]
# If nums = [0]
# Then the output will be [0].


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create value to hold index 
        insert_index = 0

        # First loop will iterate through the list and check the values of the entries 
        # If the value is equal to 0 it will continue to the next part of the code 
        # If the value is different from zero then. It will set the non-zero value at the lowest index.    
        for i in range(len(nums)):
            if nums[i] == 0:
                continue 
            else:
                nums[insert_index]=nums[i]
                insert_index+=1
                
        for i in range(insert_index,len(nums)):
            nums[i]=0
        print(nums)
