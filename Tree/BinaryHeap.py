#Creating a minHeap
class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def insert(self, value):
        self.heapList.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i = i // 2
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def percDown(self, i):
        while i * 2 <= self.currentSize:
            minChildIndex = self.minChild(i)
            if self.heapList[i] > self.heapList[minChildIndex]:
                temp = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIndex]
            i = minChildIndex
            
    def delMin(self):
        retValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retValue