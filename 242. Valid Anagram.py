class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # O(nlogn) but O(1) space
        # return sorted(s) == sorted(t)
        
        # O(n) for time and memory
        if len(s) != len(t):
            return False
        
        # return sorted(s) == sorted(t)
        lettersS = {}
        lettersT = {}

        for x in s:
            lettersS[x] += 1
        
        for x in t:
            lettersT[x] += 1
        
        return lettersS == lettersT