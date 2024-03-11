class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # bruteforce
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             count += 1
        
        # return count
        # more efficient

        count = {}
        num_good_pairs = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num in count:
            if count[num] > 1:
                for i in range(count[num]):
                    num_good_pairs += i
        
        return num_good_pairs
