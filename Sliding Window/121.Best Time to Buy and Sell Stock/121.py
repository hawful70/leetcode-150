from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = start + 1
        profit = 0

        # while end <= len(prices) - 1:
        #     if prices[start] > prices[end]:
        #         start = end
        #         end += 1
        #     else:
        #         current_profit = prices[end] - prices[start]
        #         profit = max(profit, current_profit)
        #         end += 1
        while end <= len(prices) - 1:
            if prices[start] > prices[end]:
                start = end
                end += 1
            elif prices[end] - prices[start] > profit:
                profit = prices[end] - prices[start]
                end += 1
            else:
                end += 1
        return profit
    
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))