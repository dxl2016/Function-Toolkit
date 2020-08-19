class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def count_zeros(arr):
            c = 0
            for i in range(n-1, -1, -1):
                if arr[i] == 0:
                    c += 1
                else:
                    break
            return c
        
        count = [count_zeros(arr) for arr in grid]
        ans = 0
        tmp = 0
        for i in range(n-1, -1, -1):
            target = i
            flag = 0
            if tmp<n:
                for j in range(tmp, n):
                    if count[j] >= target:
                        ans += j-tmp
                        count[tmp+1:j+1] = count[tmp:j]
                        tmp += 1
                        flag = 1
                        break
                    else:
                        continue
                if flag == 0:
                    return -1
                
        return ans

