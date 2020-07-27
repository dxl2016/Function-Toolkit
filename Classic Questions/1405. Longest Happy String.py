  
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        stock = []
        if a: heapq.heappush(stock, (-a, 'a'))
        if b: heapq.heappush(stock, (-b, 'b'))
        if c: heapq.heappush(stock, (-c, 'c'))
            
        prev_count, prev_letter = heapq.heappop(stock)
        happy = prev_letter * (1+(prev_count != -1))
        prev_count += 2
        
        while stock:
            print(happy)
            curr_count, curr_letter = heapq.heappop(stock)
            if prev_count < 0:
                heapq.heappush(stock, (prev_count, prev_letter))
            d = 1+(curr_count < (prev_count//2) and curr_count != -1)
            happy += curr_letter * d
            prev_count, prev_letter = curr_count+d, curr_letter
        
        return happy

