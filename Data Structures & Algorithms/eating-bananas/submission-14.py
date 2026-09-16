class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        speed = r

        def findHrs(k):
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)
            return t

        while l <= r:
            mid = (l + r) // 2
            hrs = findHrs(mid)
            if hrs <= h:
                speed = min(speed,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return speed
