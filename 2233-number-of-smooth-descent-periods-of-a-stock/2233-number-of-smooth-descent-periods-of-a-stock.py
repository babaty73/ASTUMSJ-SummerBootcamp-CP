class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        total_periods = 0
        current_length = 0
        
        for i in range(len(prices)):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                current_length += 1
            else:
                current_length = 1
            total_periods += current_length
            
        return total_periods
