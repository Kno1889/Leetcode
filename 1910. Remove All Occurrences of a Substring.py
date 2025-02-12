class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        new_str = ""
        n = len(part)

        for c in s:
            new_str += c
            if len(new_str) >= n:
                if new_str[-n:] == part:
                    new_str = new_str[:len(new_str) - len(part)]
        return new_str
