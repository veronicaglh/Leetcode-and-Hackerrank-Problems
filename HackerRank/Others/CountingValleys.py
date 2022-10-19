# HackerRank is a place where programmers from all over the world come together to solve different programming problems.
# All of the questions done in this folder are from the HackerRank website. 
# In order to access and solve the problems you will need to sign up for an account on their website. 
# I have also attached a link to each problem solved so you can can access the problem and attempt to solve it.
# Please run the code on HackerRanks own code editor. If you try to run it on your own IDE the code will not work.
# Here is HackerRanks website: https://www.hackerrank.com/
# Here is where you can create an account: https://www.hackerrank.com/create-account/
# This problem is called Counting Valleys
# You can acccess it here: https://www.hackerrank.com/challenges/counting-valleys/problem

# Complete the countingValleys function in the editor below.
# countingValleys has the following parameter(s):
# int steps: the number of steps on the hike
# string path: a string describing the path
# Returns: 
# int: the number of valleys traversed

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    cur_level = 0
    for steps in path:
        if(steps == 'U'):
            cur_level += 1
            if(cur_level == 0):
                valleys += 1
        elif(steps == 'D'):
            cur_level -= 1
    print(valleys)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    # fptr.write(str(result) + '\n')

    # fptr.close()
