class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # time O(n) and memory O(1)

        s = 0
        n = len(mat)

        for i in range(n):
            s += mat[i][i]
            s += mat[i][n - 1 - i]
        
        return s - (mat[n // 2][n // 2] if n % 2 == 1 else 0)
    