class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = "".join(map(str, num))

        return [int(digit) for digit in str(int(nums) + k)]