class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        sorted = []

        for i in range(len(nums)):
            sorted.append(nums[nums[i]])

        return sorted