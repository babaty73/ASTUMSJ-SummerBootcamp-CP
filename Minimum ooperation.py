#LeetCode problem 3512 minimum operation 
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums) 
        operation= total % k
        
        if operation == 0:
            return 0
        else:
            return operation
