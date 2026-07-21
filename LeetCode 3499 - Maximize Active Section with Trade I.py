#LeetCode 3499 - Maximize Active Section with Trade I
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")
        s = "1" + s + "1"
        groups = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            groups.append((s[i], j - i))
            i = j
        max_gain = 0
        for i in range(1, len(groups) - 1):
            if groups[i][0] == "1":
                if groups[i - 1][0] == "0" and groups[i + 1][0] == "0":
                    gain = groups[i - 1][1] + groups[i + 1][1]
                    max_gain = max(max_gain, gain)

        return ones + max_gain
