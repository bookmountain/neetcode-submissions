class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        timelines = self.timemap[key]
        # [["happy", 1], ["sad", 3], ["yes", 4], ["no", 7]]
        # timeMap.get("alice", 6); // return "yes"      
        l, r = 0, len(timelines) - 1
        while l <= r:
            m = (l + r) // 2
            if timelines[m][1] == timestamp:
                return timelines[m][0]
            elif timelines[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return timelines[r][0] if r >= 0 else ""

        
        
