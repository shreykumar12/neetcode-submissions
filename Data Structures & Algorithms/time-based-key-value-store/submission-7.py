class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.timemap:
            values = self.timemap[key] # list of values with key
            start = 0
            end = len(values) - 1
            while start <= end:
                mid = (start + end) // 2
                if values[mid][0] <= timestamp:
                    res = values[mid][1]
                    start = mid + 1
                elif values[mid][0] > timestamp:
                    end = mid - 1
        return res

