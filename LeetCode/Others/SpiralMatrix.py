# This problem is called 54. Spiral Matrix
# You can access it here: https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix
# The program will  return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        solution=[]
        if len(matrix)==0:
            return solution

        maxup=0
        maxdown=len(matrix)-1
        maxleft=0
        maxright=len(matrix[0])-1
        direction=0 
        
        while len(matrix):
            if direction==0:
                for i in range(maxleft,maxright+1):
                    solution.append(matrix[maxup][i])
                maxup+=1
            if direction==1:
                for i in range(maxup,maxdown+1):
                    solution.append(matrix[i][maxright])
                maxright-=1
            if direction==2:
                for i in reversed(range(maxleft,maxright+1)):
                    solution.append(matrix[maxdown][i])
                maxdown-=1
            if direction==3:
                for i in reversed(range(maxup,maxdown+1)):
                    solution.append(matrix[i][maxleft])
                maxleft+=1
            if maxup>maxdown or maxleft>maxright:
                return solution
            direction=(direction+1)%4
        return solution
        