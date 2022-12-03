# This problem is called 274. H-Index
# You can access it here: https://leetcode.com/problems/h-index/

# The program recieves an  array of integers citations where 
# citations[i] is the number of citations a researcher received 
# for their ith paper, return compute the researcher's h-index.
# Definition of h-index:
# A scientist has an index h if h of their n papers have at 
# least h citations each, and the other n − h papers have no 
# more than h citations each.
# For example: 
# If citations = [3,0,6,1,5]
# The output is 3 
# [3,0,6,1,5] means the researcher has 5 papers in total and 
# each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each 
# and the remaining two with no more than 3 citations each, their h-index is 3.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for index, citation in enumerate(citations):
            if index >= citation: 
                return index 
                
        return len(citations)