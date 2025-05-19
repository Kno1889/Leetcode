class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {" ": " "}
        letters = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for l in key:
            if l == " " or l in mapping:
                continue
            mapping[l] = letters[i]
            i += 1
        res = ""

        for c in message:
            res += mapping[c]

        return res
