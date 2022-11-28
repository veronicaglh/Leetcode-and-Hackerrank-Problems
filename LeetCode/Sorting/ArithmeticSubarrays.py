# This problem is called 1630. Arithmetic Subarrays
# You can access it here: https://leetcode.com/problems/arithmetic-subarrays/

# A sequence of numbers is called arithmetic if it consists of at least two elements, and the 
# difference between every two consecutive elements is the same. More formally, a sequence s is 
# arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
# For example: 
# The sequence = 1, 3, 5, 7, 9 is arithmetic 
# because 3 - 1 = 2 and 7 - 5 = 2 etc..
# This program will recieve an array of n integers, nums, and two arrays of m integers each, l and r,
# representing the m range queries, where the ith query is the range [l[i], r[i]].
# The program will return a list of boolean elements answer, where answer[i] is true if the subarray
# nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
# For example if nums = [4,6,5,9,3,7] and l = [0,0,2] and r = [2,3,5]
# Then the output = [true,false,true]
# Because:
# - In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
# - In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
# - In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def good(left, right):
            k = list(sorted(nums[left:right+1]))
            if len(k) == 1:
                return True

            delta = k[1] - k[0]
            for x,y in zip(k, k[1:]):
                if y - x != delta:
                    return False 
            return True 
        res = []
        for left, right in zip(l,r):
            res += [good(left, right)]
        return res