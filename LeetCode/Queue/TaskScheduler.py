# This problem is called 621. Task Scheduler
# You can access it here: https://leetcode.com/problems/task-scheduler/

# The program recieves a characters array tasks, representing the tasks a CPU 
# needs to do, where each letter represents a different task. Tasks could be 
# done in any order. Each task is done in one unit of time. For each unit of 
# time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown 
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
# The program will return the least number of units of times that the CPU will
# take to finish all the given tasks.
# For example if tasks = ["A","A","A","B","B","B"] and n = 2
# The program output will be 8
# Because: 
# - A -> B -> idle -> A -> B -> idle -> A -> B
# - There is at least 2 units of time between any two same tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:     
        count_dict = Counter(tasks)
        lst = sorted(count_dict.values(), reverse=True)
        most_common = lst[0]
        counter = 0
        i=0

        if not tasks:
            return 0

        while i<len(lst) and lst[i]==most_common:
            counter += 1
            i += 1
            
        result = (most_common - 1) * (n+1) + counter
        return max(len(tasks), result)