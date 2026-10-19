from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.system = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.system[id].append({
            "in" : stationName,
            "timeIn" : t,
            "out" : None,   
            "timeOut" : None,
            "complete" : False
        })

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        trips = self.system[id]
        for trip in trips:
            if trip["complete"]:
                continue
            else:
                trip["timeOut"] = t
                trip["out"] = stationName
                trip["complete"] = True

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        counts = 0
        val = 0
    
        for trips in self.system.values():
            for trip in trips:
                if trip["in"] == startStation and trip["out"] == endStation:
                    val += (trip["timeOut"] - trip["timeIn"])
                    counts += 1
        
        return (val / counts)
            
