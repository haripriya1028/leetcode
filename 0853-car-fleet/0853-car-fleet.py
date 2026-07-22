class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        cars=[(position[i], (target-position[i])/speed[i]) for i in range(n)]
        cars.sort(reverse=True)
        fleets=0
        curr=0
        for pos, time in cars:
            if time>curr:
                fleets+=1
                curr=time
        return fleets