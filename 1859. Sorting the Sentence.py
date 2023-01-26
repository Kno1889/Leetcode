class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ordered_sentence = ""

        words.sort(key = lambda words: words[-1])
        
        for word in words:
            ordered_sentence = ordered_sentence + word[:-1] + " "
        
        return ordered_sentence[:-1]