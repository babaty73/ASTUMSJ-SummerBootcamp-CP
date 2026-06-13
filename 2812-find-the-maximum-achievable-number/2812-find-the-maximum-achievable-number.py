class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = num + t + t
        b = x
        for i in range(t):
            num += 1
            b -= 1
            if num == b:
                break
        return x