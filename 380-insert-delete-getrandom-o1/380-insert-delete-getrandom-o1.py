class RandomizedSet:

    def __init__(self):
        self.randomizedSet={}
        
    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        else:
            self.randomizedSet[val]=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet :
            self.randomizedSet.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomizedSet.keys()))