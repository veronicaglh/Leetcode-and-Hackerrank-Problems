# This problem is called 560. Subarray Sum Equals K
# You can access it here: https://leetcode.com/problems/subarray-sum-equals-k/


# The program recieves an array of numbers called nums and an integer k.
# It will return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# For example in the array nums = [5,7,4,2,1]
# [4,2,1] or [5,7,4] is a subarray of nums. 
# Howevever  [5,1,4] is not a subarray because the values are not contiguous 
# For example if the input is:
# nums = [1,1,1] and k = 2
# The output will be 2. 
# Because there are 2 subarrays whose sum is equal to k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        result = 0
        total_sum = 0
        prefixSum = {0:1}
        
        for n in nums: 
            total_sum += n
            diff = total_sum - k 
            
            result += prefixSum.get(diff, 0)
            prefixSum[total_sum] = 1 + prefixSum.get(total_sum, 0)
            
        return result


