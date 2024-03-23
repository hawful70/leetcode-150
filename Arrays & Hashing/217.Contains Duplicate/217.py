class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}

        for num in nums:
            if num in frequency and frequency[num] >= 1:
                return True
            frequency[num] = 1

        return False