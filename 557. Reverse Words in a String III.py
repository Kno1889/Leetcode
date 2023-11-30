class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        out = []
        for word in words:

            n = len(word) - 1
            rev = ""

            while n >= 0:
                rev += word[n]
                n -= 1
            out.append(rev)

        return " ".join(out)
    