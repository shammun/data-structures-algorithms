class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.chains = [[] for _ in range(self.size)]

    def hash(self, key):
        return hash(key) % self.size
    
    def HasKey(self, object):
        chain = self.chains[self.hash(object)]
        for key, value in chain:
            if key == object:
                return True
        return False
    
    def Get(self, object):
        chain = self.chains[self.hash(object)]
        for key, value in chain:
            if key == object:
                return value
        return None
    
    def Set(self, object, value):
        chain = self.chains[self.hash(object)]
        for pair in chain:
            if pair[0] == object:
                pair[1] = value
                return
        chain.append([object, value])