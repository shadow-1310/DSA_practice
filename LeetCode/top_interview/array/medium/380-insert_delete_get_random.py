class RandomizedSet:
    def __init__(self):
        self.data = []
        self.map = {}
        
    def insert(self, val):
        flag = True
        if val in self.map:
            flag = False
        else:
            self.map[val] = len(self.data)
            self.data.append(val)
            
        return flag

    def remove(self, val):
        flag = False
        if val in self.data:
            flag = True
            index = self.map[val]
            value = self.data[-1]
            self.data[index] = value
            self.data.pop()
            self.map[value] = index
            del self.map[val]

        return flag

    def getRandom(self):
        return random.choice(self.data)
