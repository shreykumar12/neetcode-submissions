class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        self.timemap[key].append(pair)

    def get(self, key: str, timestamp: int) -> str:
        length = len(self.timemap[key])
        l, r = 0, length - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if self.timemap[key][mid][0] <= timestamp:
                res = self.timemap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1        
        return res
