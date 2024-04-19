class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(nlogn)
        # nums.sort()
        # return nums[int(len(nums) / 2)]
        
        # O(n) solution 1
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        
        # for num in counts:
        #     if counts[num] >= len(nums) / 2:
        #         return num

        # better O(n) solution
        majority = nums[0]
        maj_num = 1

        for i in range(1, len(nums)):
            if maj_num == 0:
                majority = nums[i]
                maj_num == 1

            if nums[i] == majority:
                maj_num += 1
            else: 
                maj_num -= 1
        
        return majority
