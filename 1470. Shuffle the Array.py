class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []

        for i in range(n):
            shuffled.append(nums[i]) # evens
            shuffled.append(nums[i + n]) # odds
        
        return shuffled