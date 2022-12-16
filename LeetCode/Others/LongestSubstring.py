# This problem is called 3. Longest Substring Without Repeating Characters
# You can access it here: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# The program will be given a string s
# and it will find the length of the longest substring
# without repeating characters.
# For example if s = "abcabcbb"
# The output is 3
# Because: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Checking if the string is unique
        if len(set(s)) == len(s):                       
            return len(s)
        substring = ''
        max_len = 1

        for i in s:
            if i not in substring:        
                substring = substring + i
                max_len = max(max_len, len(substring))    
            else:                                       
                substring = substring.split(i)[1] + i   

        return max_len
