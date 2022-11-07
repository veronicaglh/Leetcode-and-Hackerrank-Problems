# This problem is called 496. Next Greater Element I
# You can access it here: https://leetcode.com/problems/next-greater-element-i/

# The next greater element of some element x in an array 
# is the first greater element that is to the right of x 
# in the same array.
# The program will recieve an two integer arrays: nums1 and nums2
# where nums1 is a subset of nums2
# For each 0 <= i < nums1.length, the program will find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.
# The programm will return an array ans of which has the same length as nums1
# and ans[i] is the next greater element as described above.
# For example: if nums1 = [4,1,2] and nums2 = [1,3,4,2]
# Then the output = [-1,3,-1]
# There is no next greater element for 4 so it returns -1 
# The next greater element for 1 is is 3
# There is no next greater element for 2 so it returns -1  

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}  #num -> next greater element
        stk = []
        for i in nums2[::-1]:
            while stk and stk[-1] <= i:
                # until stk[-1] > i
                stk.pop()

            h[i] = stk[-1] if stk else -1
            stk.append(i)

        return [
            h[j]
            for j in nums1
        ]

                    
              