class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        def calc(l):
            L, mid = len(l), len(l)//2
            return sum(l[L-mid:]) - sum(l[:mid])

        houses = sorted(houses)
        n = len(houses)
        dp = [[None for _ in range(k)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = calc(houses[:i+1])

        for i in range(0,n):
            for j in range(1,k):
                if i <= j:
                    dp[i][j] = 0
                    continue
                
                dp[i][j] = dp[i][j-1]
                for t in range(0,i):
                    distance = calc(houses[t+1:i+1])
                    if dp[t][j-1]+distance < dp[i][j]:
                        dp[i][j] = dp[t][j-1]+distance

        return dp[n-1][k-1]

