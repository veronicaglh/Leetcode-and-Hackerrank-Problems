# This problem is called A. Theatre Square
# You can access it here: https://codeforces.com/problemset/problem/1/A

# Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. 
# On the occasion of the city's anniversary, a decision was taken to pave the Square with square 
# granite flagstones. Each flagstone is of the size a × a.
# What is the least number of flagstones needed to pave the Square? 
# It's allowed to cover the surface larger than the Theatre Square, 
# but the Square has to be covered. It's not allowed to break the flagstones. 
# The sides of flagstones should be parallel to the sides of the Square.
# For example if the input is 6 6 4 
# The program will be 4 

n, m, a = map(int, input().split())

if m%a == 0: 
    val1 = m // a

else: 
    val1 = m // a + 1 

if n%a == 0: 
    val2 = n // a

else: 
    val2 = n // a + 1 

print(val1*val2)  