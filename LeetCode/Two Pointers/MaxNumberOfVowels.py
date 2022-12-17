# This problem is called 1456. Maximum Number of Vowels in a Substring of Given Length
# You can access it here: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# This program wil be given  a string s and an integer k.
# It will return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# For example if  s = "abciiidef" and  k = 3
# Then the  output will be 3.
# Because: 
# - The substring "iii" contains 3 vowel letters.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel=0
        result =0

        for i in range(0,len(s)):
            if i>=k :
                if s[i-k] in ['a','e','i','o','u']:
                    result -=1

            if s[i] in['a','e','i','o','u']:
                result+=1

            max_vowel = max(max_vowel,result)
            if max_vowel == k:
                return max_vowel

        return max_vowel