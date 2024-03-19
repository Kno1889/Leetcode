class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # try:
        #     return haystack.index(needle)
        # except ValueError:
        #     return -1
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1
        