# This problem is called Grading Students
# You can acccess it here: https://www.hackerrank.com/challenges/grading/problem

# The program will accept a list of numbers(named grades) 
# and return the grades after rounding as appropriate.
# For example if input  = 4, 73, 67, 38, 33
# Then the output will be 75, 67, 40, 33

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Create list to store the rounded grades
    rounded_grades = []

    for grade in grades:
        # Code will only execute if grade is above 38
        if grade >= 38:
            # Will round appropriatly depending on the grade
            if 5 - grade % 5 < 3:
                grade += 5 - grade % 5
        rounded_grades.append(grade)

    # For loop to print each value in rounded_grades
    for i in rounded_grades:
        print(i)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
