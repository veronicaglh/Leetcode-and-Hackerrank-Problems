# This problem is called 945. Minimum Increment to Make Array Unique
# You can access it here: https://leetcode.com/problems/minimum-increment-to-make-array-unique/

# The program recieves an integer array nums. In one move, the program can pick an index i where 0 <= i < nums.length 
# and increment nums[i] by 1.
# The program will return the minimum number of moves to make every value in nums unique.
# For example: 
# If nums = [1,2,2] 
# The output is 1 
# Because, after 1 move, the array could be [1, 2, 3].

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        total = 0 
        nums.sort()

        for i in range(1, len(nums)): 
            if nums[i] <= nums[i-1]: 
                new_value = nums[i - 1] + 1
                total += new_value - nums[i]
                nums[i] = new_value 
        return total