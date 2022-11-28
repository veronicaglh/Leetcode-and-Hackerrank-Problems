# This problem is called 969. Pancake Sorting
# You can access it here: https://leetcode.com/problems/pancake-sorting/

# This program will recieve an array of integers arr, sort the array by performing a series of pancake flips.
# In one pancake flip we do the following steps:
# - Choose an integer k where 1 <= k <= arr.length.
# - Reverse the sub-array arr[0...k-1] (0-indexed).
# The program will return  an array of the k-values corresponding to a sequence of pancake flips that sort arr.
# For example if arr = [3,2,4,1]
# Then output = [4,2,4,3]
# Because: 
# - We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# - Starting state: arr = [3, 2, 4, 1]
# - After 1st flip (k = 4): arr = [1, 4, 2, 3]
# - After 2nd flip (k = 2): arr = [4, 1, 2, 3]
# - After 3rd flip (k = 4): arr = [3, 2, 1, 4]
# - After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0 
            while start < end:
                arr[start],arr[end] = arr[end], arr[start]
                start += 1 
                end -= 1 
        N = len(arr)
        output = []
        for i in range(N-1, -1, -1):
            max_ = i 
            for j in range(i, -1, -1):
                if arr[j] > arr[max_]: max_ = j 
            if max_ != i: 
                flip(max_)
                flip(i)
                output.append(max_+1)
                output.append(i+1)
        return output 