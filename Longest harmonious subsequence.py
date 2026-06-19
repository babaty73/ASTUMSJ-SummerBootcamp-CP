# leetcode problem Longest harmonious subsequence
class Solution:
    def findLHS(self, nums):
        freq = {}
        longest = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])

        return longest
