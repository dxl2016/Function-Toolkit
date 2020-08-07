class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {"a":0, "b":0, "c":0}
        pointer = 0
        ans = 0
        for i in s:
            dic[i] += 1
            while(all(dic.values()) > 0):
                dic[s[pointer]] -= 1
                pointer += 1
            
            ans += pointer
        
        return ans

