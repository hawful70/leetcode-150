class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i in range(len(nums) - 2):
            firstNum = nums[i]
            if i > 0 and firstNum == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                currentSum = firstNum + nums[left] + nums[right]
                if currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    triplets.add((firstNum, nums[left], nums[right]))
                    left, right = left + 1, right - 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets