class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num_odd = (high - low) // 2

        if (high % 2 == 1) or (low % 2 == 1):
            num_odd += 1

        return num_odd