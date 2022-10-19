# This problem is called 1004. Max Consecutive Ones III
# You can access it here: https://leetcode.com/problems/max-consecutive-ones-iii/

# This program will recieve a binary array nums and an integer k
# The program will then return the maximum number if consecutive 1's i the array 
# If the array can be flipped at most k 0's.
# For example if nums = [1,1,1,0,0,0,1,1,1,1,0] and k = 2
# Then the output will be: 6

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j=0, 0

        # float('-inf') is used to set an infinitely large value(such as positive infinity).
        final_result=float('-inf')

        # while loop will run as long as the len(nums) is not less than zero
        while j<len(nums) and i<len(nums):
            if nums[j] != 1:   
                if k>0:
                    k-=1
                else:
                    while k<0 or nums[i]==1:
                        if nums[i]==0:
                            k+=1
                        i+=1
                    i+=1
            final_result=max(final_result,j-i+1)  
            j+=1
        return final_result
        
