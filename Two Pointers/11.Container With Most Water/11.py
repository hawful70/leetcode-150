class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxContainer = 0

        while left < right:
            currentContainer = min(height[left], height[right]) * (right - left)
            maxContainer = max(maxContainer, currentContainer)
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1

        return maxContainer