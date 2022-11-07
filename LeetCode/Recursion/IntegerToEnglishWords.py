# This problem is called 273. Integer to English Words
# You can access it here: https://leetcode.com/problems/integer-to-english-words/

# The program recieves an integer value named num 
# the program will then convert num to its english word representation.
# For example num = 123
# The program will have an output of: "One Hundred Twenty Three"

class Solution:
    def numberToWords(self, num: int) -> str:
        one_nineteen = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        TENS_VALUE = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        if num == 0: return "Zero"
        
        else:
            def recursor(num):
                if num==0: return ""
                
                if num<=19: return one_nineteen[num-1]

                if num<=99: return (TENS_VALUE[num//10-2]+ " " + recursor(num%10)).rstrip() 

                if num <=999: return (recursor(num//100) + " Hundred "+ recursor(num%100)).rstrip() 

                if num <=10**6-1: return (recursor(num//1000) + " Thousand "+ recursor(num%1000)).rstrip() 

                if num <=10**9-1: return (recursor(num//(10**6)) + " Million "+ recursor(num%(10**6))).rstrip() 

                else: return (recursor(num//(10**9)) + " Billion "+ recursor(num%(10**9))).rstrip() 
            
            return recursor(num)
