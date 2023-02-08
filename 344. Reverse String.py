class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tail_ind = len(s) - 1
        head_ind = 0
        
        while(tail_ind > head_ind):
            temp = s[head_ind]
            s[head_ind] = s[tail_ind]
            s[tail_ind] = temp

            head_ind += 1
            tail_ind -= 1
