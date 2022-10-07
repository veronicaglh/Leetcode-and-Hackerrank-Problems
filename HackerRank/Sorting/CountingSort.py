# This problem is called Counting Sort 1
# You can acccess it here: https://www.hackerrank.com/challenges/countingsort1/problem

# The Counting Sort program will accept a list of numbers(named arr) and return another list with the same length as arr. 
# The second list (named result_list) will contain the number of times an element is found in the first list(arr) 
# based on each respective index. 
# For example if arr = [1,1,3,2,1] 
# Then result_ list = [0, 3, 1, 1]
# Meaning the number 0 appeared 0 times in the arr list 
# The number one appeared 3 times in the arr list 
# The number two appeared once in the arr list etc....

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    result_list= []
    for i in range(len(arr)): 
        result_list.append(0)
    for i in arr:
        result_list[i] += 1
    for i in range(len(result_list)):
        print(result_list[i], end=' ')
    
          
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    # n represents the length of the list arr
    # arr represents the list of numbers

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

