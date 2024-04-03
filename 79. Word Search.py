class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # recursion
        # Recursive backtracking: check the first character, then check neighbors if correct

        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(row_i, col_i, word_i):
            if word_i == len(word):
                return True
            
            if (row_i < 0 or col_i < 0 or row_i >= rows or col_i >= cols):
                return False
            
            if word[word_i] != board[row_i][col_i]:
                return False
            
            if (row_i, col_i) in path:
                return False
            
            path.add((row_i, col_i))

            check_neighbors = (dfs(row_i + 1, col_i, word_i + 1) 
            or dfs(row_i - 1, col_i, word_i + 1) 
            or dfs(row_i, col_i + 1, word_i + 1)
            or dfs(row_i, col_i - 1, word_i + 1))

            path.remove((row_i, col_i))

            return check_neighbors
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False

        