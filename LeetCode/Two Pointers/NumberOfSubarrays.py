# This problem is called 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# You can access it here: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

# The program will be given an array of integers arr and two integers k and threshold.
# It will then return the number of sub-arrays of size k and average greater than or equal to threshold. 
# For example if  arr = [2,2,2,2,5,5,5,8], k = 3 and threshold = 4
# Then the output will be 3
# Because: 
# - Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays 
#   of size 3 have averages less than 4 (the threshold).

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        sum_threshold = k * threshold
        cur_sum = sum(arr[:k])
        result = 0

        if cur_sum >= sum_threshold:
            result += 1

        for i in range(k, len(arr)):
            cur_sum -= arr[i - k]
            cur_sum += arr[i]
            if cur_sum >= sum_threshold:
                result += 1

        return result