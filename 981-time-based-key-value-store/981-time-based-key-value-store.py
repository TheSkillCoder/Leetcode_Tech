class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key]=dict()
            self.time_map[key]["times"]=[]
        self.time_map[key][timestamp] = value
        self.time_map[key]["times"].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            if timestamp in self.time_map[key]:
                return self.time_map[key][timestamp]
            else:
                times=self.time_map[key]["times"]
                start, end = 0, len(times)-1
                if times[end]<timestamp:
                    return self.time_map[key][times[end]]
                elif times[start]>timestamp:
                    return ""
                x=-1
                while(start<end):
                    mid = (start+end)//2
                    if times[mid]>timestamp:
                        end=mid-1
                    elif times[mid]<timestamp:
                        x=mid
                        start=mid+1
                return self.time_map[key][times[x]]
        return ""
      