class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, path, res):
            if l < 0 or r < 0 or l > r:
                return
            if l == 0 and r == 0:
                res.append(path)
                return 
            
            dfs(l-1, r, path+"(", res)
            dfs(l, r-1, path+")", res)
        
        res = []
        dfs(n, n, "", res)
        
        return res
        
        
