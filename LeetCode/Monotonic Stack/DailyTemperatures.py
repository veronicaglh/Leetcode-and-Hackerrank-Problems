# This problem is called 739. Daily Temperatures
# You can access it here: https://leetcode.com/problems/daily-temperatures/

# The program recieves an array of integers named temperatures. 
# The values in temperatures represents the daily temperatures.
# It will return an array answer such that answer[i] is the number of days you have to wait 
# after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, the program will keep answer[i] == 0 instead.
# For example: if temperatures = [73,74,75,71,69,72,76,73]
# Then the output = [1,1,4,2,1,1,0,0]
# If temperatures = [30,40,50,60]
# The the program will return [1,1,1,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = []
        for i in range(len(temperatures)):
            ans.append(0)
            
        for i, t in enumerate(temperatures):
          while stack and t > temperatures[stack[-1]]:
            index = stack.pop()
            ans[index] = i - index
          stack.append(i)

        return ans