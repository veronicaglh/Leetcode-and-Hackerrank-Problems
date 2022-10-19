# This problem is called 238. Product of Array Except Self
# You can access it here: https://leetcode.com/problems/product-of-array-except-self/


# The program recieves integer array nums, return another integer array answer.
# Each value in answer(answer[i]) will be the will be the product of all the numbers except nums[i]. 
# For example if nums = [1,2,3,4] 
# Then answer = [24,12,8,6]
# The program will return the second list.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create empty list answer to store the products
        answer = []
  
        if len(nums) == 0:
            return

        # Declare variable counter = 1
        # So that when nums[i] is intially multiplied it can be multiplied with 1
        # And counter will be gradually incremented with each multiplication process.
        counter = 1

        # For each item in nums append 1 into answer 
        for i in range(len(nums)):
            answer.append(1)

        # Counter will be multiplied with each value in num 
        # And the value of counter will be set as answer[i]
        for i in range(len(answer)):
            answer[i] = counter
            counter *= nums[i]
            

        # Initialize counter to 1 for product on right side
        counter = 1

        # Count variable contains product of
        # elements on right side excluding arr[i]
        for i in range(len(answer) - 1, -1, -1):
            answer[i] *= counter
            counter *= nums[i]
        
        return answer
        
        