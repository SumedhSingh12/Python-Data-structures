class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)

class Queue2Stacks(object):
    
    def __init__(self):
        
        self.in_stack = Stack()
        self.out_stack = Stack()
     
    def enqueue(self, element):
        self.in_stack.push(element)
    
    def dequeue(self):
        if self.out_stack.size() == 0:
            while self.in_stack.size() > 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print (q.dequeue())