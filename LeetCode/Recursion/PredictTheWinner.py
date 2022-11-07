# This problem is called 486. Predict the Winner
# You can access it here: https://leetcode.com/problems/predict-the-winner/

# The program will be given an integer array nums.
# Two players are playing a game with this array: player 1 and player 2.
# Player 1 and player 2 take turns, with player 1 starting first. Both
# players start the game with a score of 0. At each turn, the player 
# takes one of the numbers from either end of the array (i.e., nums[0] 
# or nums[nums.length - 1]) which reduces the size of the array by 1. 
# The player adds the chosen number to their score. The game ends when 
# there are no more elements in the array.
# The program will return true if Player 1 can win the game. 
# If the scores of both players are equal, then player 1 
# is still the winner, and the program will also return true
# For example if nums = [1,5,2]
# The program will return false

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        total = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if i == j:
                    total[i][j] = nums[i]
                else:
                    total[i][j] = max(nums[i] - total[i+1][j], nums[j] - total[i][j-1])
        
        return total[0][-1] >= 0

        