# This problem is called 1338. Reduce Array Size to The Half
# You can access it here: https://leetcode.com/problems/reduce-array-size-to-the-half/

# This program will recieve integer array arr.
# The program can choose a set of integers and remove all the occurrences of these integers in the array.
# It will then return the minimum size of the set so that at least half of the integers of the array are removed.
# For example if arr = [3,3,3,3,5,5,5,2,2,7]
# Then output = 2
# Because: 
# - Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# - Possible sets of size 2 are {3,5},{3,2},{5,2}.
# - Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half 
# of the size of the old array.

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        N = len(arr)
        n = 0
        output = 0 
        for k,v in sorted(c.items(), key=lambda x: -x[1]):
            n+=v
            output += 1
            if n >= (N//2): break 
        return output 




