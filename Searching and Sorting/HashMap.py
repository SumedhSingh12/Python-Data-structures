class HashMap:
    
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, value):
        
        hashValue = self.hashFunction(key, self.size)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
        
        elif self.slots[hashValue] == key:
            self.data[hashValue] = value
        
        else:
            nextHash = self.reHash(hashValue, self.size)
            
            while self.slots[nextHash] != None and self.slots[nextHash] !=key:
                nextHash = self.reHash(nextHash, self.size)
                
            if self.slots[hashValue] == None:
                self.slots[hashValue] = key
                self.data[hashValue] = value
        
            else: 
                self.data[hashValue] = value
                
    def hashFunction(self, key, size):
        return key % size
    
    def reHash(self, oldHash, size):
        return (oldHash + 1) % size
    
    def get(self, key):
        startSlot = self.hashFunction(key, self.size)
        stop = False
        found = False
        position = startSlot
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                return self.data[position]
            else:
                position = self.reHash(position, self.size)
                if position == startSlot:
                    stop = True
        return self.data[position]
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        return self.put(key,data)
            