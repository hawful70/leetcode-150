class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        # left, right = 0, 10**9
        left, right = 0, nums[-1] - nums[0]
        ans = 10**9
        
        print(nums[-1])
        while left <= right:
            mid = left + (right - left) // 2
            if self.isValidDifference(nums, p, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    def isValidDifference(self, nums: List[int], p: int, threehold: int):
        i, count = 0, 0
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= threehold:
                count += 1
                i += 2
            else:
                i += 1
            if count == p:
                return True
        return False