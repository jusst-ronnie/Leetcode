import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        
        for l, r, h in buildings:
            events.append((l, -h, r))  # start
            events.append((r, 0, 0))   # end
        
        events.sort()
        
        res = []
        heap = [(0, float('inf'))]  # (height, end)
        prev = 0
        
        for x, neg_h, r in events:
            
            while heap[0][1] <= x:
                heapq.heappop(heap)
                
            if neg_h:
                heapq.heappush(heap, (neg_h, r))
            
            curr = -heap[0][0]
            
            if curr != prev:
                res.append([x, curr])
                prev = curr
                
        return res