class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = 0
        le = 0
        
        for i in range(len(nums)):
            if nums[i] > threshold:
                l = i + 1
            elif i > l and nums[i] % 2 == nums[i - 1] % 2:
                l = i if nums[i] % 2 == 0 else i + 1
            if l <= i and nums[l] % 2 != 0:
                l = i + 1
            if l <= i:
                le = max(le, i - l + 1)
                
        return le
