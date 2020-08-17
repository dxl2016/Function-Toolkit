class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k, n = 2, len(prices)
        if n < 2:
            return 0

        buy = [[-float('Inf')]*(k+1) for _ in range(n)]
        sell = [[0]*(k+1) for _ in range(n)]
        for i in range(n):
            for j in range(k,0,-1):
                if i == 0:
                    buy[i][j] = -prices[i]
                    continue
                buy[i][j] = max(buy[i-1][j], sell[i-1][j-1]-prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j]+prices[i])
        
        return sell[n-1][k]

