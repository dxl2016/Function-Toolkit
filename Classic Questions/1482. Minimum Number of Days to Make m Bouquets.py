  
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay:
            return 0
        
        days = sorted(set(bloomDay))
        n = len(days)
        l, r = 0, n-1
        
        def search(bloomDay, mid_day, l, r, curr_m, curr_k):
            temp = []
            for i,k in enumerate(bloomDay):
                if k <= mid_day:
                    if not temp:
                        temp.append(i)
                    else:
                        if temp[-1] == i-1:
                            temp.append(i)
                        else:
                            curr_m -= len(temp)//curr_k
                            temp = []
                            temp.append(i)
            if temp:
                curr_m -= len(temp)//curr_k
            if curr_m <= 0:
                return True
            else:
                return False
        
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            mid_day = days[mid]
            if search(bloomDay, mid_day, l, r, m, k):
                ans = mid_day
                r = mid-1
            else:
                l = mid+1
        
        return ans

