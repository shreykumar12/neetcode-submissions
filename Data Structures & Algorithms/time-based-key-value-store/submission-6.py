class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (value, timestamp)
        self.store[key].append(pair)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        size = len(self.store[key])
        l, r = 0, size - 1

        while l <= r:
            m = (l + r ) // 2
            if self.store[key][m][1] <= timestamp:
                res = self.store[key][m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
