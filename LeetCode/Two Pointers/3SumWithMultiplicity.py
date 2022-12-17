# This problem is called 923. 3Sum With Multiplicity
# You can access it here: https://leetcode.com/problems/3sum-with-multiplicity/

# The program is given an integer array arr, and an integer target.
# It will then return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
# It is important to note the answer can be very large, return it modulo 109 + 7.
# For example if arr = [1,1,2,2,3,3,4,4,5,5] and target = 8
# Then the output will be: 20
# Because:
# - Enumerating by the values (arr[i], arr[j], arr[k]):
# - (1, 2, 5) occurs 8 times;
# - (1, 3, 4) occurs 8 times;
# - (2, 2, 4) occurs 2 times;
# - (2, 3, 3) occurs 2 times.

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        kMod = 1_000_000_007
        ans = 0
        count = collections.Counter(arr)

        for i, x in count.items():
            for j, y in count.items():
                k = target - i - j
                if k not in count:
                    continue
                if i == j and j == k:
                    ans = (ans + x * (x - 1) * (x - 2) // 6) % kMod
                elif i == j and j != k:
                    ans = (ans + x * (x - 1) // 2 * count[k]) % kMod
                elif i < j and j < k:
                    ans = (ans + x * y * count[k]) % kMod

        return ans % kMod

