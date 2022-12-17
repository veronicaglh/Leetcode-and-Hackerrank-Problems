# This problem is called 948. Bag of Tokens
# You can access it here: https://leetcode.com/problems/bag-of-tokens/

# The program is given an initial power of power, an initial score of 0, 
# and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).
# The program will maximize your total score by potentially playing each token in one of two ways:
# - If the current power is at least tokens[i], it will play the ith token face up, 
#   losing tokens[i] power and gaining 1 score.
# - If the current score is at least 1, it will play the ith token face down, 
#   gaining tokens[i] power and losing 1 score.
# Each token may be played at most once and in any order. It is not mandatory to play 
# all the tokens.
# The program will return the largest possible score that is possible to achieve after 
# playing any number of tokens.
# For example if tokens = [100] and power = 50
# Then the output will be: 0
# Because:
# - Playing the only token in the bag is impossible because you either have too little
#   power or too little score.

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        L, H = 0, len(tokens)-1
        score, res = 0, 0
        while L <= H:
            if tokens[L] <= power:
                power-=tokens[L]
                score+=1
                res = max(score, res)
                L+=1
            elif score >= 1:
                power+=tokens[H]
                score-=1
                H-=1
            else:
                break
        return res
