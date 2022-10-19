# This problem is called 3. Longest Substring Without Repeating Characters
# You can access it here: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# This program will recieve a string s and find the length of the longest substring 
# that does not have repeating characters.
# For example if s = "abcabcbb" 
# The output will be 3 
# Because the longest substring without repeating characters in string s is "abc"
# which has a length of 3. 
# For example if s = "pwwkew"
# The output will be 3 
# Because the longest substring without repeating characters is "wke"
# which has a length of 3. 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # First need to check if the string is unique
        if len(set(s)) == len(s):                       
            return len(s)
        substring = ''
        maxLen = 1

        for i in s:
            # If given character is not in substring it will be added to the substring
            # maxlength will be updated if our substring is longer than the current max.
            # If the character is already part of the substring
            # we create a new substring from that is built from the next character
            # Process repeats till the loop terminates(when i in no longer in s)
            if i not in substring:        
                substring = substring + i
                maxLen = max(maxLen, len(substring))    
            else:                                       
                substring = substring.split(i)[1] + i   
        return maxLen
