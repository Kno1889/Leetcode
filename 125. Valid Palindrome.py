class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        s_size = len(s)
        half_size = s_size // 2

        for i in range(half_size):
            if not s[i] == s[s_size - i - 1]:
                return False
        
        return True
        