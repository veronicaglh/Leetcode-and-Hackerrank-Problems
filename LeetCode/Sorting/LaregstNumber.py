# This problem is called 179. Largest Number
# You can access it here: https://leetcode.com/problems/largest-number/

# This program will recieve a list of non-negative integers nums. It will then arrange them so that
# they are arranged in a way that these numbers form the largest possible number. 
# It will then return this number as a string
# For example if nums = [10,2]
# Then output =  "210"
# For example if nums = [3,30,34,5,9]
# Then output =  "9534330"

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(num1,num2):
            if num1 + num2 > num2 + num1:
                return -1 

            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))
