class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not sorted(list(set(nums))) == sorted(nums)
