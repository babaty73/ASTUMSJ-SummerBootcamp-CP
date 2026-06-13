class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        counts = str(nums).count(str(digit)) 
        return(counts)