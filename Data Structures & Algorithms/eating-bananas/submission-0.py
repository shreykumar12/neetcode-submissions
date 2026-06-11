class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko can eat a maximum of max(piles) bananas in an hour
        # We can run binary search on all piles (1 - max(piles)) 
        # To find the minimum # of bananas she can eat an hour to finish under h

        start, end = 1, max(piles)
        res = max(piles)

        def findHrs(k):
            hrs = 0
            for pile in piles:
                hrs += ((pile + k - 1) // k)
            return hrs
        
        while start <= end:
            mid = int((start + end) / 2)
            hrs = findHrs(mid)
            if hrs <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return res