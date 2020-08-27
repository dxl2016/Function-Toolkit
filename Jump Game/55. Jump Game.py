class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= temp: 
                temp = i
        return temp == 0
