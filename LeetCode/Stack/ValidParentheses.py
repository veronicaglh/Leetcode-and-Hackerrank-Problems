# This problem is called 20. Valid Parentheses
# You can access it here: https://leetcode.com/problems/valid-parentheses/

# This program will recieve a string value which will contain characters like '(', ')', '{', '}', '[' and ']'. 
# The program will then display if the string is valid or not.  
# The string will only be valid if these three conditions are satisfied: 
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# For example lets say the name of the variable that stores the string is s. 
# If s =  "()"
# Then the program returns true. 
# If s = "(]"
# Then the program returns false. 


class Solution:
    def isValid(self, s: str) -> bool:
        
        # Create dictionary(named characters) to store all the characters of the string
        # the keys will be the opening characters 
        # and the closing characters will be the values. 
        # The list result_stack will contain all the opening characters in string s 
        characters = {'(':')', '{':'}','[':']'}
        result_stack = []

        if len(s)%2 != 0 or len(s)==0:
            return False
            
        for i in s:
            if i in characters.keys() :
                # will only append the characters found in the key of the dictionary(i.e the opening characters)
                result_stack.append(i)
                
            # if the character is not in the key of the dictionary 
            # then the program will pop the last value in result_stack 
            # and store it in a variable named key_character. 
            # then since all the values stored in result_stack are keys in the dictionary 
            # we can find the value of those keys by using characters[key_character]
            # which will return the value of key_character 
            # For Eg: lets say key_character = ( 
            # then characters[(] = ) 
            # The program then checks if the closing value is in the string s 
            # if it is it returns True
            # if it is not it returns False 
            else:
                if len(result_stack)== 0:
                    return False
                key_character = result_stack.pop()
                
                if i!=characters[key_character]:
                    return False
        return result_stack == []