class Solution:
    def countDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return 1
        count = 0
        digits = [*str(num)]

        for i in digits:
            if num % int(i) == 0:
                count += 1

        return count
