class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = start + 1

        res = 0
        while end <= len(prices) - 1:
            if prices[start] > prices[end]:
                start = end
                end += 1
            else:
                currentProfit = prices[end] - prices[start]
                res = max(res, currentProfit)
                end += 1
        
        return res