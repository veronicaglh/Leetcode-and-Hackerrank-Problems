# This problem is called 1859. Sorting the Sentence. 
# You can access it here: https://leetcode.com/problems/sorting-the-sentence/


# The sorting the sentence program recieves a sentence 
# in which all the words of that sentence have been rearranged incorrectly
# and stored in variabe called s. 
# The program will then correctly rearrange the words and store them in a list called sorted_sentence. 
# For eg if this is s = "is2 sentence4 This1 a3"
# This is sorted_sentence = ["This", "is", "a","sentence"]
# The program should output "This is a sentence"


class Solution:
    def sortSentence(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        # The split method splits a string into seperate words 
        # Those words would then be appended to a list named words
        words = s.split()
        result = []
        sorted_sentence = []
        
        for number in range(10): 
            for i in range(len(words)):
                if f"{number}" in words[i]: 
                    result.append(words[i])
                    
                    
        for i in range(len(result)): 
            result_correct = result[i].translate({ ord(c): None for c in "123456789" })
            if i == 0: 
                sorted_sentence.append(f'{result_correct}')
            elif i == len(result) - 1: 
                sorted_sentence.append(f'{result_correct}')
            else: 
                sorted_sentence.append(result_correct)
        

        answer = ' '.join(sorted_sentence)
        return answer