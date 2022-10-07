# This problem is called Insertion Sort - Part 1
# You can access it here: https://www.hackerrank.com/challenges/insertionsort1/problem

# The Insertuon Sort program will accept a list of intergers. The name of this list is arr 
# The values in arr have all been sorted(in ascending order) expect for the very last cell
# The insertion sort algorithm will then attempt to place the value of the last cell in its correct place
# For example if list arr = [1, 2, 4, 5, 3]
# Then the final result will be the following: 
# 1 2 4 5 5
# 1 2 4 4 5
# 1 2 3 4 5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # The variable right_most_cell will hold the value of the last cell of list arr
    # array_one is the list that will hold the final result 
    right_most_cell = arr[n - 1]
    array_one = []
    
    for i in reversed(range(n)): 
        if arr[i] > right_most_cell:
            arr[i+1] = arr[i] 

        if arr[i] < right_most_cell:
            arr[i+1] = right_most_cell
            
        for j in range(len(arr)):
            if j <= 4: 
                array_one.append(arr[j])
                
    for i in range(len(array_one)):
        if i != 0 and i != 1 and i != 2 and i != 3 and i != 4:
            print(array_one[i], end=" ")
            if i == 9 or i == 14 or i == 19 or i == 24:
                print("")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # n refers to the length of the list arr 
    # arr refers to the list of the numbers 

    insertionSort1(n, arr)

