class Solution1:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        return nums[int(len(nums) / 2)]
    
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num in counts:
            if counts[num] >= len(nums) / 2:
                return num