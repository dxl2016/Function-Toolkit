class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr)%2 != 0:
            return False
        tmp = [0 for _ in range(k)]
        for i in arr:
            tmp[i%k] += 1
        if tmp[0]%2 != 0:
            return False
        if k>1:
            c = 1
            while(c<=k//2):
                if tmp[c] != tmp[k-c]:
                    return False
                c += 1
        return True

