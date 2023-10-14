class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            result = []
            for i, x in enumerate(nums):
                if x == target:
                    result.append(i)
            return [result[0], result[-1]]
        else:
            return [-1, -1]
