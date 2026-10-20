from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.trips = defaultdict(lambda:[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.active[id]
        self.trips[(startStation, stationName)][0] += (t - startTime)
        self.trips[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.trips[(startStation, endStation)][0]
        trips = self.trips[(startStation, endStation)][1]
        return time / trips
