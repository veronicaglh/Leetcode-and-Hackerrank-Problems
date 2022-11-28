# This problem is called 11. Container With Most Water
# You can access it here: https://leetcode.com/problems/container-with-most-water/

# The program recieves an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# The program will Find two lines that together with the x-axis 
# form a container, such that the container contains the most water.
# The program will return the maximum amount of water a container can store.
# For example if height = [1,8,6,2,5,4,8,3,7]
# Then the  output will be 49.
# Because: 
# - The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# - In this case, the max area of water (blue section) the container 
# - can contain is 49.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0 
        l, r = 0, len(height) - 1

        while l < r:
            area = (r-l) * min(height[l], height[r])
            result = max(result,area)

            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1
        return result
