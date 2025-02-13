class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num: int) -> int:
            digit_sum = 0
            for c in str(num):
                digit_sum += int(c)
            return digit_sum

        i, j = 0, 0        
        pairs = False
        max_sum = get_digit_sum(nums[i])

        for k in range(1, len(nums)):
            dig_sum = get_digit_sum(nums[k])
            
            if dig_sum > max_sum:
                pairs = False
                i = k
                max_sum = dig_sum
            
            elif dig_sum == max_sum:
                pairs = True
                j = k
            
        return nums[i] + nums[j] if pairs else -1
