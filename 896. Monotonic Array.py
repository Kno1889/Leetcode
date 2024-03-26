class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # worse time O(nlogn), better memory
        # return nums == sorted(nums) or nums == sorted(nums, reverse = True)
        
        # better time O(n), worse memory
        
        non_dec = True
        non_inc = True

        # non_increasing => next number should be less than or equal to
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                non_inc = False
                break
        
        # non_decreasing => next number should be greater than or equal to
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                non_dec = False
                break

        return non_dec or non_inc
