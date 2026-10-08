class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) # 5
        r = sum(weights) # 19
        res = 0

        def findDays(weight):
            curr_total = 0
            numDays = 1
            for w in weights:
                if curr_total + w > weight:
                    numDays += 1
                    curr_total = w
                else:
                    curr_total += w
            print(weight, numDays)
            return numDays

        while l <= r:
            mid = (l + r) // 2
            numDays = findDays(mid)
            if numDays <= days:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res