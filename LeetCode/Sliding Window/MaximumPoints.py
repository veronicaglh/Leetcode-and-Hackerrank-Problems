# This problem is called 1423. Maximum Points You Can Obtain from Cards
# You can access it here: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# There are several cards arranged in a row, and each card has an associated number of points. 
# The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. 
# You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
# For example if cardPoints = [1,2,3,4,5,6,1] and k = 3
# Then the output will be 12

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_pointer, right_pointer = 0, len(cardPoints) - k
        total = sum(cardPoints[right_pointer:])
        final_result = total 

        while right_pointer < len(cardPoints):
            total+= (cardPoints[left_pointer] - cardPoints[right_pointer])
            final_result = max(final_result, total)
            left_pointer += 1
            right_pointer += 1 
        return final_result