class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        n = len(needle)
        h = len(haystack)
        
        while l <= h - n:
            if haystack[l : l + n] == needle:
                return l
            else:
                l += 1
                
        return -1
