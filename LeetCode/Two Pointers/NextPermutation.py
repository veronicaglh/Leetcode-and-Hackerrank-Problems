# This problem is called 31. Next Permutation
# You can access it here: https://leetcode.com/problems/next-permutation/

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of arr: 
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
# then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is
# not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# This program will be given an array of integers nums and will find the next permutation of nums.
# The replacement will be in place and use only constant extra memory.
# For example if nums = [1,2,3]
# Then the  output will be [1,3,2]
# For example if nums = [3,2,1]
# Then the  output will be [1,2,3]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        while i >= 0:
            if nums[i] >= nums[i + 1]:
                i -= 1
            else:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        return
        nums.reverse()