class Solution:
    def maxScore(self, s: str) -> int:
        # def left_sum(substring):
        #     l_sum = 0
        #     for c in substring:
        #         if c == "0":
        #             l_sum += 1
        #     return l_sum
        
        # def right_sum(substring):
        #     r_sum = 0
        #     for c in substring:
        #         if c == "1":
        #             r_sum += 1
        #     return r_sum
        
        # max_sum = 0
        # for i in range(1, len(s)):
        #     new_sum = left_sum(s[:i]) + right_sum(s[i:])
        #     if new_sum > max_sum:
        #         max_sum = new_sum
        # return max_sum
        max_sum = 0

        for i in range(1, len(s)):
            new_sum = s[:i].count("0") + s[i:].count("1")
            if new_sum > max_sum:
                max_sum = new_sum
        return max_sum