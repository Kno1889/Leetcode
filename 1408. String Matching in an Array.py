class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring = []
        for word in words:
            i = 0

            while(i < len(words)):
            # for i in range(len(words)):
                if word in words[i] and word != words[i] and word not in substring:
                    substring.append(word)
                i += 1
        return substring
