class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        speed = end

        def getHours(k):
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)
            return t

        while start <= end:
            mid = (start + end) // 2
            hrs = getHours(mid)
            if hrs <= h:
                speed = min(speed, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return speed

            