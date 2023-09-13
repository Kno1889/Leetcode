class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bruteforce, O(n^2) time but O(1) memory
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]

        # Better, O(n) time, but worse memory O(n)
        nums_map = {}

        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                return [i, nums_map[target - nums[i]]]

            nums_map[nums[i]] = i
