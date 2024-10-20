class HitCounter:

    def __init__(self):
        self.hashmap=defaultdict(int)
        

    def hit(self, timestamp: int) -> None:
        self.hashmap[timestamp]+=1
        

    def getHits(self, timestamp: int) -> int:
        list1=list(self.hashmap.keys())
        res=0
        for key in list1:
            if key>timestamp-300:
                res+=self.hashmap[key]

        return res
