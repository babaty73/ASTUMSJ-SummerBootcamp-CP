class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        r = len(patterns)
        for ch in patterns:
            if ch not in word:
                r -= 1
        return(r)