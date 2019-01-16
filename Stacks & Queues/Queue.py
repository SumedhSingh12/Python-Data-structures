class Queue(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        remove_num = self.items[0]
        self.items.remove(remove_num)
        return remove_num
    
q = Queue()