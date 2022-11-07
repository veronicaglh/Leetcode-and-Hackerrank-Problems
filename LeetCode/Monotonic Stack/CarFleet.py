# This problem is called 853. Car Fleet
# You can access it here: https://leetcode.com/problems/car-fleet/

# There are n cars going to the same destination along a one-lane road. 
# The destination is target miles away.
# There are two integer arrays: position and speed. 
# Both the arrays have the same length n.
# position[i] is the position of the ith car
# and speed[i] is the speed of the ith car (in miles per hour).
# A car can never pass another car ahead of it, but it can catch up to it 
# and drive bumper to bumper at the same speed. 
# The faster car will slow down to match the slower car's speed. 
# The distance between these two cars is ignored (i.e., they are assumed to have the same position).
# A car fleet is some non-empty set of cars driving at the same position and same speed. 
# Note that a single car is also a car fleet.
# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
# The program will return the number of car fleets that will arrive at the destination.
# For example if target = 12 and position = [10,8,0,5,3] and speed = [2,4,1,1,3]
# The the program will output 3
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, 
# meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        answer = 0 
        current = 0
        for i in reversed(cars):
            if i > current:
                answer += 1
                current = i
        return answer
        
        