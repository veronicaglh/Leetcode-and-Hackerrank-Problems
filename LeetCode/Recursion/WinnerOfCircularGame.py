# This problem is called 1823. Find the Winner of the Circular Game
# You can access it here: https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# There are n friends that are playing a game. The friends are sitting in a circle and 
# are numbered from 1 to n in clockwise order.
# More formally, moving clockwise from the ith friend brings you to the (i+1)th friend 
# for 1 <= i < n, and moving clockwise from
# the nth friend brings you to the 1st friend.
# The rules of the game are as follows:
# Start at the 1st friend.
# Count the next k friends in the clockwise direction including the friend you started at. 
# The counting wraps around the circle 
# and may count some friends more than once.
# The last friend you counted leaves the circle and loses the game.
# If there is still more than one friend in the circle, go back to step 2 starting from 
# the friend immediately clockwise of the 
# friend who just lost and repeat.
# Else, the last friend in the circle wins the game.
# The program will be given the number of friends, n, and an integer k.
# It will then return the winner of the game.
# For example: if n = 5, k = 2
# Then the output will be 3 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n + 1)]

        def rec(index, k):
            if len(arr) == 1:
                return 
            index = (index + k)%len(arr)
            arr.pop(index)
            rec(index,k)

        rec(0, k-1)
        return arr[0]
