class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.person = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id] = [stationName, t]
      
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time_taken = t - self.person[id][1]
        tup = (self.person[id][0], stationName)
        if tup not in self.times:
            self.times[tup] = [time_taken, 1]
            del self.person[id]
        else:
            self.times[tup][0] += time_taken
            self.times[tup][1] += 1
            del self.person[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tup = (startStation, endStation)
        return self.times[tup][0] / self.times[tup][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)