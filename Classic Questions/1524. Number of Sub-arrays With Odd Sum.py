class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even = 0
        odd = 0
        for v in arr:
            if v%2 == 0:
                even, odd = even + 1, odd
            else:
                even, odd = odd, even + 1
            ans = (ans+odd)%(10**9+7)
        
        return ans%(10**9+7)

