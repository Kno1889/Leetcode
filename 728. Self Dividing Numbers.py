class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int):
            if "0" in str(num):
                return False
            
            for digit in str(num):
                if num % int(digit) != 0:
                    return False
            return True
        self_dividing = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                self_dividing.append(num)
        
        return self_dividing
        