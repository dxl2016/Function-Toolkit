class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        end = len(nums)-1
        for i in range(len(nums)):
            while(nums[i]+nums[end]>target):
                if end>i:
                    end -= 1
                else:
                    return ans%(10**9+7)
            ans += pow(2, end-i)
            
        return ans%(10**9+7)

