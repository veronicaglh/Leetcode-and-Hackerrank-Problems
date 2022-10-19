# This problem is called 1365. How Many Numbers Are Smaller Than the Current Number
# You can access it here: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# This program will recieve a list of integers(named nums)
# The program will display another list which will show how many numbers is less than each number in the original list 
# For example if nums = [8,1,2,2,3]
# Then result =  [4,0,1,1,3]
# Meaning there are 4 numbers less than the number 8 in the initial list (nums)
# There are no numbers less than the number one in the nums list 
# There is 1 number less than the number 2 in the nums list etc..
# The program will output the result list 

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        count = 0 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]  < nums[i]:
                    count += 1
            result.append(count)
            count = 0
        return result 
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 