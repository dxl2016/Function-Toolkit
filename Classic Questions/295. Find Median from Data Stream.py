class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.half_min = []
        self.half_max = []

    def addNum(self, num: int) -> None:
        if not self.half_max:
            heapq.heappush(self.half_max, num)
        elif not self.half_min:
            tmp = heapq.heappop(self.half_max)
            if num > tmp:
                heapq.heappush(self.half_max, num)
                heapq.heappush(self.half_min, -tmp)
            else:
                heapq.heappush(self.half_max, tmp)
                heapq.heappush(self.half_min, -num)
        else:
            tmp1 = heapq.heappop(self.half_max)
            tmp2 = -heapq.heappop(self.half_min)
            l = sorted([tmp1, tmp2, num])
            heapq.heappush(self.half_min, -l[0])
            heapq.heappush(self.half_max, l[2])
            if len(self.half_min) >= len(self.half_max):
                heapq.heappush(self.half_max, l[1])
            else:
                heapq.heappush(self.half_min, -l[1])
    
    def findMedian(self) -> float:
        if len(self.half_max) == len(self.half_min):
            return (self.half_max[0]-self.half_min[0])/2.0
        elif len(self.half_max) > len(self.half_min):
            return self.half_max[0]
        else:
            return -self.half_min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

