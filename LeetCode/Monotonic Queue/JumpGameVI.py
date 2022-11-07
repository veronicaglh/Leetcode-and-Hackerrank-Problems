# This problem is called 1696. Jump Game VI
# You can access it here: https://leetcode.com/problems/jump-game-vi/

# The program recieves an array of integers named nums and an integer value k.
# A playerof the game is initially standing at index 0. In one move
# they can jump at most k steps forward without going outside the boundaries of the array. 
# That is, they can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
# The goal is to reach the last index of the array (index n - 1). Their score will be the sum of all 
# nums[j] for each index j they have visited in the array.
# The program will return the maximum score they can get 
# For example if nums = [1,-1,-2,4,-7,3] and k = 2
# The program will return 7 
# Because they can choose their jumps forming the 
# subsequence [1,-1,4,3]. The sum is 7.

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        deq = deque([len(nums)-1])
        for i in range(len(nums)-2, -1, -1):
            if deq[0] - i > k: deq.popleft()
            nums[i] += nums[deq[0]]
            while len(deq) and nums[deq[-1]] <= nums[i]: deq.pop()
            deq.append(i)
        return nums[0]
