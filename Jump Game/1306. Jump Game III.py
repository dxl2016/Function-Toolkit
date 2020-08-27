class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(idx):
            if arr[idx] == 0:
                self.ans = True
                return
            else:
                if idx not in seen:
                    seen.add(idx)
                    if 0 <= idx+arr[idx] < n:
                        dfs(idx+arr[idx])
                    if 0 <= idx-arr[idx] < n:
                        dfs(idx-arr[idx])
                else:
                    return

        if 0 not in arr:
            return False
        if arr[start] == 0:
            return True
        n = len(arr)
        seen = set()
        self.ans = False
        dfs(start)
        
        return self.ans

