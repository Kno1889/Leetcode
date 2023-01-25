def decimalToBase(number, base):
    number_in_base = ""

    while number > 0:
        digit = int(number%base)

        if digit < 10:
            number_in_base += str(digit)
        else:
            number_in_base += chr(ord('A') + digit - 10)

        number //= base

    return number_in_base[::-1]

def isPalindromic(number :str) -> bool:
    left = 0
    right = len(number) - 1

    while (left < right):
        if number[left] != number[right]:
            return False

        left += 1
        right -= 1
    return True


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            if not isPalindromic(decimalToBase(n, base)):
                return False
        return True
