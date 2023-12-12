class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bruteforce would be a nested for loop
        max_prod = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (((nums[i] - 1) * (nums[j] - 1)) > max_prod) and (i != j):
                    max_prod = (nums[i] - 1) * (nums[j] - 1)
        
        return max_prod
    
        