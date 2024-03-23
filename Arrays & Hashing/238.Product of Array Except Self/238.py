class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        left_sum = 1
        right_sum = 1
        for i in range(1, len(nums)):
            left_sum *= nums[i - 1]
            ans[i] *= left_sum
        for i in range(len(nums)-2, -1, -1):
            right_sum *= nums[i + 1]
            ans[i] *= right_sum
            
        return ans