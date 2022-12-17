# This problem is called 845. Longest Mountain in Array
# You can access it here: https://leetcode.com/problems/longest-mountain-in-array/

# An array arr is a mountain array if and only if:
# - arr.length >= 3
# - There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# This program wil be given an integer array arr
# and will return the length of the longest subarray,
#  which is a mountain. It will return 0 if there is no mountain subarray.
# For example if arr = [2,1,4,7,3,2,5]
# Then the  output will be 5.
# Because: 
# - The largest mountain is [1,4,7,3,2] which has length 5.

class Solution:
  def longestMountain(self, A: List[int]) -> int:
    ans = 0
    i = 0

    while i + 1 < len(A):
      while i + 1 < len(A) and A[i] == A[i + 1]:
        i += 1

      increasing = 0
      decreasing = 0

      while i + 1 < len(A) and A[i] < A[i + 1]:
        increasing += 1
        i += 1

      while i + 1 < len(A) and A[i] > A[i + 1]:
        decreasing += 1
        i += 1

      if increasing > 0 and decreasing > 0:
        ans = max(ans, increasing + decreasing + 1)

    return ans

