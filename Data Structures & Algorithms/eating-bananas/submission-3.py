class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start, end = 1, max(piles)
        res = max(piles)

        def findHrs(k):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            return hrs
        
        
        while start <= end:
            mid = (start + end) // 2
            hrs = findHrs(mid)
            if hrs <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return res
