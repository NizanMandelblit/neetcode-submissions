class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force
        # speed = 1
        # while True:
        #     totalTime = 0 
        #     for p in piles:
        #         totalTime += math.ceil(p / speed)
            
        #     if totalTime <= h:
        #         return speed
            
        #     speed += 1 # Try the next speed

        l, r = 1, max(piles)

        totalHours = 0
        res = max(piles)

        while l<=r:
            k = l + ((r-l)//2)
            totalHours=0
            for p in piles:
                totalHours += math.ceil(p/k)
            if totalHours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1 
        return res