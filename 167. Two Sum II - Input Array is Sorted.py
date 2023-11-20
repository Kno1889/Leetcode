class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # j = len(numbers) - 1

        # for i in range(len(numbers) - 1):
        #     for j in range(i, len(numbers)):
        #         if numbers[i] + numbers[j] == target and i != j:
        #             return [i + 1, j + 1]

        nums = {} # number, index

        for i in range(len(numbers)):
            if target - numbers[i] in nums.keys():
                return [nums[target - numbers[i]] + 1, i + 1]
            nums[numbers[i]] = i
        

        