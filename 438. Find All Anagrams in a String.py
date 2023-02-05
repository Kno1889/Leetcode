def getCharacterCount(s: str) -> Dict[str, int]:
        return {character: s.count(character) for character in set(s)}

class Solution:    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices_list = []

        p_chars = getCharacterCount(p)

        for i in range(len(s)):
            if getCharacterCount(s[i: i + len(p)]) == p_chars:
                indices_list.append(i)
        
        return indices_list