class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for w in word:
            if not w in "0123456789":
                word = word.replace(w, " ")
        
        ints = [int(w) for w in word.split()]

        return len(set(ints))