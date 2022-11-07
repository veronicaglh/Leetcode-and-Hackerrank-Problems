# This problem is called 443. String Compression
# You can access it here: https://leetcode.com/problems/string-compression/

# The program recieves an array named chars and compresses it using the following algorith,:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# After modifying the input array, It will return the new length of the array.
# For example if chars = ["a","a","b","b","c","c","c"]
# The output: Return 6, and the first 6 characters of the input array 
# should be: ["a","2","b","2","c","3"]

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        index = 0 
        while i < len(chars):
            j = i 
            while j < len(chars) and chars[j] == chars[i]:
                j+= 1

            chars[index] = chars[i]
            index += 1 

            count = j - i
            if count > 1: 
                for c in str(count):
                    chars[index] = c
                    index += 1 

            i = j 
        chars = chars[:index]
        return index