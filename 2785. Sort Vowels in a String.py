class Solution:

    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        temp = ""
        s_vow = []
        
        for c in s:
            if c in vowels: # found a vowel
                temp += "1" # placeholder
                s_vow.append(ord(c)) 
            else:
                temp += c
        
        s_vow.sort()
        t = ""
        j = 0
        for i in range(len(temp)):
            if temp[i] == "1":
                t += chr(s_vow[j])
                j += 1
            else:
                t += temp[i]
           
        return t