class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def compress(s: str) -> str:
            new_str = ""
            count_dict = {}
            for i in s:
                if i in count_dict:
                    count_dict[i] += 1
                else:
                    count_dict[i] = 1
            
            for i in count_dict:
                new_str += str(i) + str(count_dict[i])
            
            return new_str
        
        compressed_str = compress(s)
        