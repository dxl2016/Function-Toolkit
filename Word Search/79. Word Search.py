class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return
        
        def dfs(i, j, idx, count):
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[idx]:
                return
            count += 1
            if count == l:
                return True
            c = board[i][j]
            board[i][j] = "0"
            if dfs(i+1, j, idx+1, count):
                return True
            if dfs(i-1, j, idx+1, count):
                return True
            if dfs(i, j+1, idx+1, count):
                return True
            if dfs(i, j-1, idx+1, count):
                return True
            
            board[i][j] = c
            return False

        m, n = len(board), len(board[0])
        l = len(word)
        self.ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, 0):
                        return True
                
        return False

