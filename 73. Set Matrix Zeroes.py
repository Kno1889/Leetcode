class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Bruteforce: make a copy matrix and modify. O(mn) memory. Worst time
        # Improvement: add another row and another column to indicate whether we need to set the corresponding row/column to 0. O(m+n) memory and O(mn) time
        # Solution: O(1) mem, O(mn) time. Place padding row/column inside existing matrix. Overlapping cell is what necessitates extra memory. Pattern: Iterate across matrix and determine which rows/cols need to be zero

        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False

        # detemrine which rows/cols need to be zero'ed out
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # set element in row 0 of this column to 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        # zero out most rows/cols as necessary, except first row/col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # zero out firs col if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # zero out first row if needed
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
