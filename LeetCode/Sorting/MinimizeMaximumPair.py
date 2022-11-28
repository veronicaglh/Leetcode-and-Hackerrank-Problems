# This problem is called 1877. Minimize Maximum Pair Sum in Array
# You can access it here: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum 
# in a list of pairs.
# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be
#  max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# This program will recieve a list of integers, nums of even length n 
# It will then pair up the elements of nums into n / 2 pairs such that:
# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# The program will return the minimized maximum pair sum after optimally pairing up the elements.
# For example if nums = [3,5,2,3]
# Then output = 7
# Because: 
# - The elements can be paired up into pairs (3,3) and (5,2).
# - The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = 0 

        index = 0 
        size = len(nums)-1 

        while index <size:
            max_pair = max(max_pair, nums[index]+ nums[size])
            index += 1 
            size -= 1

        return max_pair 

