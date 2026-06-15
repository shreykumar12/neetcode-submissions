class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                if values[mid][0] == timestamp:
                    return values[mid][1]
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid -1
        
        return res