class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x, y in points:
            dist= x*x+y*y

            heapq.heappush(heap, (-dist, [x,y]))
            if len(heap)>k:
                heapq.heappop(heap)
            
        res=[]
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
        