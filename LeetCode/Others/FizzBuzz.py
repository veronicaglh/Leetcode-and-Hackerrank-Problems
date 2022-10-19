# This problem is called 412. Fizz Buzz
# You can access it here: https://leetcode.com/problems/fizz-buzz/

# The program recieves an integer n
# return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Create list to store either "FizzBuzz", "Fizz" or "Buzz"
        result = []

        # For loop will iterate and append the word depending on the divisibility of num. 
        # After loop terminates the final result list with all the appropriate values will be returned. 
        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 == 0:
                result.append("FizzBuzz")
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(num))

        return result