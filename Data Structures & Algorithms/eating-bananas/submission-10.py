class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def findHrs(k):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            return hrs

        while l <= r:
            m = (l + r) // 2
            hrs = findHrs(m)

            if hrs <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res