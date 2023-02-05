class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices_list = []

        for i in range(len(s)):
            if sorted(s[i: i + len(p)]) == sorted(p):
                indices_list.append(i)
        
        return indices_list