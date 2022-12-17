# This problem is called 763. Partition Labels
# You can access it here: https://leetcode.com/problems/partition-labels/

# The program is given a string s. It will then partition the string into as many parts 
# as possible so that each letter appears in at most one part.
# The partition is done so that after concatenating all the parts in order, 
# the resultant string should be s.
# The program will return a list of integers representing the size of these parts.
# For example if s = "ababcbacadefegdehijhklij"
# Then the output will be: [9,7,8]
# Because:
# - The partition is "ababcbaca", "defegde", "hijhklij".
# - This is a partition so that each letter appears in at most one part.
# - A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end = 0
        parts_size = []
        last_occurrence_index = [None] * 26
        n = len(s)
        
        for i in range(n):
            last_occurrence_index[ord(s[i]) - ord('a')] = i
            

        for i in range(n):
            end = max(end, last_occurrence_index[ord(s[i]) - ord('a')])
            
            if i == end:
                parts_size.append(end - start + 1)
                start = end + 1
                
        return parts_size
