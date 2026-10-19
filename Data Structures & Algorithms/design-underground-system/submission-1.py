from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.routeTotals = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        fromStation, fromTime = self.active[id]
        self.routeTotals[(fromStation, stationName)][0] += (t - fromTime)
        self.routeTotals[(fromStation, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.routeTotals[(startStation, endStation)][0]
        trips = self.routeTotals[(startStation, endStation)][1]
        return time / trips
        
