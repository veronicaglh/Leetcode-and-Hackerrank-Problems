# This problem is called 347. Top K Frequent Elements
# You can access it here: https://leetcode.com/problems/top-k-frequent-elements/

# This program will recieve  an integer array nums and an integer k.
# The program will return the k most frequent elements. 
# The answer can be returned in any order.
# For example if nums = [1,1,1,2,2,3] and k = 2
# Then output = [1,2]
# For example if nums = [1] and k = 1
# Then output = [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums) == k: 
            return nums 

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get )