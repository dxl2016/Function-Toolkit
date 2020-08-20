class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, stack):
            # print(stack)
            if not s:
                return True
            if s in stack:
                return stack[s]
            
            res = False
            for word in wordDict:
                if s.startswith(word):
                    if len(s) == len(word):
                        res |= True
                    else:
                        res |= dfs(s[len(word):], stack)
            
            stack[s] = res
            return res
        
        return dfs(s, {})

