class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        left, right = 1, n
        ans = 0
        while left <= right:
            mid = (left + right) // 2

            coins = (mid / 2) * (mid + 1)
            if coins <= n:
                left = mid + 1
                ans = max(mid, ans)
            else:
                right = mid - 1
        return ans