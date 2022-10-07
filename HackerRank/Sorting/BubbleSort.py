# HackerRank is a place where programmers from all over the world come together to solve different programming problems.
# All of the questions done in this folder are from the HackerRank website. 
# In order to access and solve the problems you will need to sign up for an account on their website. 
# I have also attached a link to each problem solved so you can can access the problem and attempt to solve it.
# Please run the code on HackerRanks own code editor. If you try to run it on your own IDE the code will not work.
# Here is HackerRanks website: https://www.hackerrank.com/
# Here is where you can create an account: https://www.hackerrank.com/create-account/
# The first problem is called Bubble Sort. You can access it here: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

# The Bubble Sort program will attempt to sort a list of integers in increasing order. 
# The name of the list containing the integers is a
# The program will also store the number of swaps(or the number of tries) it took to sort the list in ascending order
# The program will also display the first and last numbers of the sorted list.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):  
    # The list count_swaps will count the number of swaps it takes to sort the list.
    # With every iteration a number will be appeneded to the count_swaps list 
    # and the length of the list will be equivalent to the number of swaps it took to arrange the list in ascending order.
    count_swaps=[]
    for i in range(n):
        for j in range(n - 1):
            if a[j] >  a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count_swaps.append(j)

    print(f"Array is sorted in {len(count_swaps)} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n - 1]}")
        
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    # n rerfers to the length of list a
    # while a is the list containing integer values that havent not yet been sorted. 
    countSwaps(a)

