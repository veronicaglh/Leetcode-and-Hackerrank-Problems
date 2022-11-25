# This problem is called 1985. Find the Kth Largest Integer in the Array
# You can access it here: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

# This program will recieve a list of strings(named nums) and another integer value named k.
# Each value in nums is represents an integer that does not have a leading zero
# The program will return the number in the form of string that represents the kth laregst 
# integer in nums
# For example if nums = ["3","6","7","10"] and k = 4
# The then program is asked to find the 4th largest integer in nums 
# which will be 3. 
# This will be easier to find if we first sort nums. 
# It will return the number as a string 
# so the output will be "3"

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # create empty list nums_list
        # to store the number values in nums
        nums_int = []

        # convert values in nums from string into integer datatype 
        # and append to nums_int list 
        for i in nums:
            nums_int.append(int(i))

        # sort the nums_int 
        # index value will be the index of the answer
        nums_int.sort()
        index_value = len(nums) - k
        return str(nums_int[index_value])

