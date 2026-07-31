class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones=[-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            largest=-heapq.heappop(stones)
            second=-heapq.heappop(stones)
            if largest!=second:
                heapq.heappush(stones, -(largest-second))
        return -stones[0] if stones else 0