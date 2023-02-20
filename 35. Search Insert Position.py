class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            left_index = 0
            right_index = len(nums) - 1

            while left_index <= right_index:
                mid_index = (left_index + right_index) // 2

                if nums[mid_index] < target:
                    left_index = mid_index + 1
                else:
                    right_index = mid_index - 1

            return left_index
