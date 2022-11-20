# This problem is called 2089. Find Target Indices After Sorting Array
# You can access it here: https://leetcode.com/problems/find-target-indices-after-sorting-array/

# This program will recieve a list of integers(named nums) and another integer value named target.
# A target index is an index i such that nums[i] == target.
# The program will return a list of the target indices of nums after sorting nums in non-decreasing order. 
# For example if nums = [1,2,5,2,3] and target = 2
# Then result =  [0,2]
# Beacause After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if target == nums[i]:
                output.append(i)

        return output


            
    







            
    
