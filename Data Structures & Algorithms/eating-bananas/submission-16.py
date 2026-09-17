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
            m = (l + r) // 2
            hrs = findHrs(m)
            if hrs <= h:
                speed = min(m, speed)
                r = m - 1
            else:
                l = m + 1
        
        return speed