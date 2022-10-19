# This problem is called 904. Fruit Into Baskets
# You can access it here: https://leetcode.com/problems/fruit-into-baskets/

# This program will recieve an array of integers named fruits 
# The trees are represented by the mentioned integer array fruits 
# where fruits[i] is the type of fruit the ith tree produces.
# There are only two baskets
# and each basket can only hold a single type of fruit 
# Starting from any tree, you must pick exactly one fruit from every tree (including the start tree) 
# while moving to the right. 
# The picked fruits must fit in one of your baskets.
# Once there is a tree with fruit that cannot fit in the baskets, program must terminate.
# which has a length of 3. 
# The program will then return the the maximum number of fruits that can be picked.
# For example if fruits = [1,2,1]
# Then the output will be 3 
# Because it is permitted to pick from all three trees.  

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start,end,max_len = 0, 0, 0
        d = {}
        while end<len(fruits):
            d[fruits[end]] = end
            if len(d) >= 3:
                min_val = min(d.values())
                del d[fruits[min_val]]
                start = min_val + 1
                
            max_len = max(max_len, end - start + 1)
            end += 1 
        return max_len