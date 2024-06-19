class Solution:
    def isHappy(self, n: int) -> bool:
        current = str(n)
        seen = set()

        while not current in seen:
            seen.add(current)
            new = 0

            for digit in current:
                new += int(digit) ** 2
            current = str(new)

            if current == "1":
                return True
        
        return False
            