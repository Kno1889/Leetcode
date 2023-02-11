class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str_1 = ""
        str_2 = ""

        for substr in word1:
            str_1 += substr
        
        for substr in word2:
            str_2 += substr
        
        return str_1 == str_2
