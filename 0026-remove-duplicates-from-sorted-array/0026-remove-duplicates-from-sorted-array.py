class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = set(nums)
        k = len(new)
        undu = len(nums) - k
        nums[:] = sorted(list(new))

        return(k)
        