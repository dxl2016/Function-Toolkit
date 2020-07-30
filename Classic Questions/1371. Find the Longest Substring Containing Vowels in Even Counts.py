class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # comb: 2**5
        tmp = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        # print(bin(1))
        # print(bin(2))
        # print(bin(4))
        # print(bin(8))
        # print(bin(16))
        
        memo = {0:-1}
        res = 0
        ans = 0
        for k,v in enumerate(s):
            if v in tmp:
                res ^= tmp[v]
            
            if res not in memo:
                memo[res] = k
            else:
                ans = max(ans, k-memo[res])
        print(memo)
        
        return ans

