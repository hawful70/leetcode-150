class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left, right = 0, n - 1

        while left <= right:
            square_left = nums[left] * nums[left]
            square_right = nums[right] * nums[right]

            if square_left > square_right:
                ans[right - left] = square_left
                left += 1
            else:
                ans[right - left] = square_right
                right -= 1
        return ans

