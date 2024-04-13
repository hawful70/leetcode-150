class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verifySpeedToComplete(speed):
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / speed)
                if hours > h:
                    return False
            return hours <= h

        left, right = 1, max(piles)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if verifySpeedToComplete(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans