# This problem is called 1512. Number of Good Pairs
# You can access it here: https://leetcode.com/problems/number-of-good-pairs/

# The program recieves an array of integers called nums and returns the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Where i and j are the index and nums[i] and nums[j] is the value in the nums list. 
# For example if nums = [1,2,3,1,1,3] 
# The output will be 4
# Because there are 4 good pairs 
# The 4 good pairs are (0,3), (0,4), (3,4), (2,5) 
# At (0,3) the 0th index value is 1 while the 3rd index value is also 1
# Since 1 = 1 and 0 < 3 this satisfies the requirement hence it is considered a good pair
# The program will return the number of good pairs. 

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Create list numsl to store all the values of num
        # Create result list to store all the good pairs.
        numsl = []
        result = []
        
        # Append each value in nums to numsl 
        for i in nums:
            numsl.append(i)

        # Compare the values in numsl and in nums    
        for i in range(len(numsl)):
            for j in range(len(nums)):
                # If the values are similar and the index of the first value is less than the second value 
                # It will append the index pair (For example: (0,3)) into the result list.
                if numsl[i] == nums[j] and i < j:
                    result.append(f"({i},{j})")

        # The program will then return the length of result 
        # Which is the number of good pairs             
        return len(result)
       

        