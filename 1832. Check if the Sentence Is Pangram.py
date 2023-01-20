class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter not in sentence:
                return False
        return True