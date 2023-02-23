class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count_dict = {nums.count(num):num for num in nums}

        return count_dict[1]
