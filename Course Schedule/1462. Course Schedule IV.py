class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not queries:
            return
        if not prerequisites:
            return [False]*len(queries)
        
        temp = {}
        for i in range(n):
            temp[i] = []
            
        for i,j in prerequisites:
            try:
                temp[i] += [j]
            except:
                temp[i] = [j]
        
        result = []  
        @lru_cache(None)
        def dp(nxt, target):
            if nxt == target:
                return True
            return any(dp(nxt_nxt, target) for nxt_nxt in temp[nxt])

        for x,y in queries:
            result.append(dp(x, y))

        return result

