class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bruteforce would be a nested for loop
        # max_prod = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (((nums[i] - 1) * (nums[j] - 1)) > max_prod) and (i != j):
        #             max_prod = (nums[i] - 1) * (nums[j] - 1)
        
        # return max_prod

        # Alt, faster O(n) method
        largest, largest2 = 0, 0

        for num in nums:
            if num > largest:
                largest2 = largest
                largest = num
            elif num > largest2:
                largest2 = num
        
        return (largest - 1) * (largest2 - 1)
                