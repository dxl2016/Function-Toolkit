class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s, stack):
            print(stack)
            if not s:
                return []
            if s in stack:
                return stack[s]
            
            res = []
            for word in wordDict:
                if s.startswith(word):
                    if len(s) == len(word):
                        res.append(word)
                    else:
                        rest = dfs(s[len(word):], stack)
                        for each in rest:
                            res.append(word + " " + each)
            
            stack[s] = res
            return res
    
        return dfs(s, {})

    
