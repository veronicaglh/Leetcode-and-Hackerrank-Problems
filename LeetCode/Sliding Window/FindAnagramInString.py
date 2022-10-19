# This problem is called 438. Find All Anagrams in a String
# You can access it here: https://leetcode.com/problems/find-all-anagrams-in-a-string/

# This program will recieve two strings s and p 
# The program will then return an array of all the start indices of p's 
# anagrams in s
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# For example if s = "cbaebabacd" and p = "abc"
# Then the output will be [0,6]
# Because the string at the start index(0) is "cba", which is an anagram of "abd" 
# while moving to the right. 
# The string with the start index(6) is "bac" which is also an anagram of "abc"

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_c = Counter(p)
        anagrams = []
        it = iter(s)
        sliding_window = deque(islice(it, len(p)), maxlen=len(p))

        s_c = Counter(sliding_window)

        if s_c == p_c:
            anagrams.append(0)

        for index, char in enumerate(it, start=1):
            s_c[char] += 1
            s_c[s[index-1]] -= 1
            if s_c == p_c:
                anagrams.append(index)
        return anagrams
 