class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high % 2 == 1) or (low % 2 == 1):
            return 1 + (high - low) // 2

        return (high - low) // 2
