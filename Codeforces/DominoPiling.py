# This problem is called A. Domino piling
# You can access it here: https://codeforces.com/problemset/problem/50/A

# The program is given a rectangular board of M × N squares. And an unlimited number of standard 
# domino pieces of 2 × 1 squares. It is allowed to rotate the pieces. The program is required to place as many 
# dominoes as possible on the board so as to meet the following conditions:
# 1. Each domino completely covers two squares.
# 2. No two dominoes overlap.
# 3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.
# The program will find the maximum number of dominoes, which can be placed under these restrictions.
# For example if the input is 2 4 
# The program will be 4 

m, n = map(int, input().split())
print(m*n//2)
