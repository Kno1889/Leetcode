class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            if sentence.count(" ") > max_words:
                max_words = sentence.count(" ")
        
        return max_words + 1