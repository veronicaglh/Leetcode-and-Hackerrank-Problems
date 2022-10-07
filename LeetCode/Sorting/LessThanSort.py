# LeetCode is a place where programmers from all over the world come together to solve different programming problems.
# All of the questions done in this folder are from the LeetCode website. 
# In order to access and solve the problems you will need to sign up for an account on their website. 
# I have also attached a link to each problem solved so it is possible to access the problem and attempt to solve it.
# Please run the code on LeetCodes own code editor. If you try to run it on your own IDE the code will not work.
# Here is LeetCodes website: https://leetcode.com/
# Here is where you can create an account: https://leetcode.com/accounts/signup/
# This problem is called 1365. How Many Numbers Are Smaller Than the Current Number
# You can access it here: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# This program will recieve a list of integers(named nums)
# The program will display another list which will show how many numbers is less than each number in the original list 
# For example if nums = [8,1,2,2,3]
# The program then will output : [4,0,1,1,3]
# Meaning there are 4 numbers less than the number 8 in the initial list (nums)
# There are no numbers less than the number one in the nums list 
# There is 1 number less than the number 2 in the nums list etc..

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        nums_zero = []
        nums_one = []
        nums_two = []
        nums_three = []
        nums_four = []
        
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j] < nums[i]:
                    if i == 0:
                        nums_zero.append(nums[j])
                
                    elif i == 1:
                        nums_one.append(nums[j])

                    elif i == 2:
                        nums_two.append(nums[j])

                    elif i == 3:
                        nums_three.append(nums[j])

                    elif i == 4:
                        nums_four.append(nums[j])


        final_nums = [len(nums_zero), len(nums_one), len(nums_two), len(nums_three),len(nums_four)]
        return final_nums
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 