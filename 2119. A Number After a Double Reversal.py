def reverseNum(n: int) -> int:
    return int("".join(reversed(str(n))))


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return reverseNum(reverseNum(num)) == num
