class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(speed):
            hours=0
            for n in piles:
                hours+=(n+speed-1)//speed
            return hours<=h
        
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            if canEat(mid):
                right=mid-1
            else:
                left=mid+1
        
        return left