# This problem is called 150. Evaluate Reverse Polish Notation
# You can access it here: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# This program will solve an arithmetic expression in Reverse Polish Notation.
# The valid operators are +, -, *, and /. 
# The program will recieve a list named tokens which will contain all the numbers as well as operations to be performed.
# The program will then solve the expression and return the result 
# For eg if tokens  = ["2","1","+","3","*"]
# Then the program will return 9
# Because ((2 + 1) * 3) = 9
# If tokens = ["4","13","5","/","+"]
# Then the program will return 6
# Because (4 + (13 / 5)) = 6

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # The int_list will store all the same values as the tokens list
        # But the numbers have now been converted to integer data type 
        # Intially in the tokens list all the values were of string data type 
        # The result_tokens list will contain the final result 
        int_list = []
        result_tokens = []
        
        # This for loop is so that the elements in tokens can be converted to integer data type
        # It will attempt to convert the elements in the tokens list into an integer 
        # If it can not do that(for example: when the element is an operand such as "*", "/", "+" or "-")
        # It will append to the int_list either way. 
        for i in range(len(tokens)):
            try:
                int_val = int(tokens[i])
                int_list.append(int_val)
            except:
                int_list.append(tokens[i])
                
        # The second for loop is to solve the expression
        # While iterating through the int_list if the value is different from an operator 
        # Then that value gets appended to the result_tokens list. 
        # If that value is an operator however the program will perform the necessary operation 
        # and append the result to result_tokens.     
        for i in int_list: 
            if i != '+' and i != '*' and i!='/' and i!='-':
                result_tokens.append(i)
            else:
                if i == '+':
                    result_tokens.append(result_tokens.pop() + result_tokens.pop())
                    
                if i == '-':
                    second_num = result_tokens.pop()
                    first_num = result_tokens.pop() 
                    result_tokens.append(first_num -  second_num)
                    
                if i == '*':
                    result_tokens.append(result_tokens.pop() * result_tokens.pop())
                    
                if i == '/':
                    second_num = result_tokens.pop()
                    first_num = result_tokens.pop() 
                    result_tokens.append(int(first_num/second_num))
                    
        
        final_answer =' '.join(str(j) for j in result_tokens)
        return final_answer

                
                
        
