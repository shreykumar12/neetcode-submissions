class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = 0

        def findDays(weight):
            curr = 0
            days = 1
            for w in weights:
                if curr + w > weight:
                    days += 1
                    curr = w
                else:
                    curr += w
            return days
                

        while l <= r:
            mid = (l + r) // 2
            nDays = findDays(mid)
            if nDays <= days:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        
        return res