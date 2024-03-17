class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = s[0]
        key_changes = 0

        for i in range(1, len(s)):
            if s[i].lower() == prev.lower():
                continue
            else:
                key_changes += 1
                prev = s[i]

        return key_changes  
        