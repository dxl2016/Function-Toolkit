class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = set()
        ans = []
        last = collections.defaultdict(int)
        
        for each in names:
            k = last[each]
            modified = each
            while(modified in res):
                k += 1
                modified = each + "(" + str(k) + ")"
            last[each] = k
            
            ans.append(modified)
            res.add(modified)
        
        return ans

