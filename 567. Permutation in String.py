def getCharCount(s: str) -> dict[str, int]:
    return {character: s.count(character) for character in set(s)}

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s2_substring_len = len(s1)

        s1_char_count = getCharCount(s1)

        for i in range(len(s2)):
            if getCharCount(s2[i:i + s2_substring_len]) == s1_char_count:
                return True
        return False
