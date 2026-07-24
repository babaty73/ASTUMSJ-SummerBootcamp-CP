#LeetCode problem 3867: Sum of GCD of Formed Pairs
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        prefix = [0] * n
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefix[i] = gcd(nums[i], mx)
        prefix.sort()
        ans = 0
        for i in range(n // 2):
            ans += gcd(prefix[i], prefix[n - 1 - i])
        return ans
