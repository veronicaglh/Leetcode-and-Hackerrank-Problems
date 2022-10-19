# This problem is called 304. Range Sum Query 2D - Immutable
# You can access it here: https://leetcode.com/problems/range-sum-query-2d-immutable/


# The program recieves a 2D matrix matrix
# It will then calculate the sum of the elements of matrix inside the rectangle defined 
# by its upper left corner (row1, col1) and lower right corner (row2, col2). 
# int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the elements of matrix inside the rectangle. 
# For example if the input is: 
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2],  [1, 2, 2, 4]]
# Then the output will be: 
# [null, 8, 11, 12]
# Because sumRegion(2, 1, 4, 3) will return 8 
# Because sumRegion(1, 1, 2, 2) will return 11 
# Because sumRegion(1, 2, 2, 4) will return 12 

class NumMatrix:
  def __init__(self, matrix: List[List[int]]):
    if len(matrix)==0:
        return
    
    self.prefix = [[0] * (len(matrix[0]) + 1) for r in range(len(matrix) + 1)]

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        self.prefix[i + 1][j + 1] = \
            matrix[i][j] + self.prefix[i][j + 1] + \
            self.prefix[i + 1][j] - self.prefix[i][j]

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - \
        self.prefix[row2 + 1][col1] + self.prefix[row1][col1]