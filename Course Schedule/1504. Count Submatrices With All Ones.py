class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        tmp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n-1, -1, -1):
                if j == n-1:
                    tmp[i][j] = mat[i][j]
                else:
                    if mat[i][j] > 0:
                        tmp[i][j] = tmp[i][j+1] + 1
        # print(tmp)
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    width = sys.maxsize
                    for k in range(i, m):
                        width = min(width, tmp[k][j])
                        ans += width
        return ans

