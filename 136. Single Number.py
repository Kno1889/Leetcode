class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # time O(n), but also space
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq.keys():
            if freq[num] == 1:
                return num
        