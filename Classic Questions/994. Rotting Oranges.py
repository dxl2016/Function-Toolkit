class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        c = 0
        for i,j in product(range(m), range(n)):
            if grid[i][j] == 2:
                q.append((i,j))
            if grid[i][j] == 1:
                c += 1
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        ans = 0
        
        while(q):
            ans += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in direction:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        c -= 1
                        grid[x+dx][y+dy] = 2
                        q.append((x+dx, y+dy))
                        
        return -1 if c != 0 else max(ans-1, 0)

