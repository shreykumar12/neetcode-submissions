class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1 
        end = speed = max(piles)

        while start <= end:
            mid = (start + end) // 2 #
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / mid)
            if hrs <= h:
                speed = min(speed, mid)
                print(speed)
                end = mid - 1
            else:
                start = mid + 1
        
        return speed