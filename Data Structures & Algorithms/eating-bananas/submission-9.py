class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        
        def findHrs(k):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            return hrs

        while l <= r:
            mid = (l + r) // 2
            hrs = findHrs(mid)
            
            if hrs <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res


