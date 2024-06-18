class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) == 1:
            return weights[0]
        
        left = max(weights)
        right = sum(weights)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if self.validWeightCapacity(days, weights, mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def validWeightCapacity(self, days: int, weights: List[int], weight_capacity: int):
        days_shipped = 1
        capacity = weight_capacity
        for weight in weights:
            if weight > capacity:
                days_shipped += 1
                capacity = weight_capacity
            capacity -= weight
        return days_shipped <= days
